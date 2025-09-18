# app/webhooks/line.py
from fastapi import APIRouter, Header, HTTPException, Request
from fastapi.responses import JSONResponse

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from app.config import settings
from app.utils.line_sig import verify_line_signature
from app.utils.time import to_dt_from_ms
from app.services.langgraph import build_prompt, get_agent_graph

router = APIRouter()
_line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
_parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@router.post("/webhook")
async def webhook(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    if not verify_line_signature(settings.LINE_CHANNEL_SECRET, body, x_line_signature):
        raise HTTPException(status_code=400, detail="Invalid LINE signature")
    try:
        events = _parser.parse(body.decode("utf-8"), x_line_signature)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Parse error: {e}")

    results = []
    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
            uid = event.source.user_id
            user_text = (event.message.text or "").strip()
            
            lc_messages = build_prompt(user_text)

            graph = await get_agent_graph()
            try:
                out_state = await graph.ainvoke({"messages": lc_messages, "uid": uid})
                ai_msg = out_state["messages"][-1]
                reply_text = getattr(ai_msg, "content", str(ai_msg))
            except Exception as e:
                reply_text = f"Sorry, I hit an error running the model: {e}"

            try:
                _line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text[:5000]))
            except Exception:
                reply_text += "\n\n(Note: Unable to send reply via LINE API.)"

            results.append({"uid": uid, "result": reply_text})

    return JSONResponse({"ok": True, "results": results})
