# app/services/langgraph.py
from __future__ import annotations
import json, time
from typing import Dict, List, Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, AIMessage, SystemMessage, BaseMessage

from app.config import settings

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    uid: str

def build_prompt(new_user_text: str, history_docs: list[dict]=[]) -> List[BaseMessage]:
    msgs: List[BaseMessage] = [SystemMessage(
        content=settings.SYSTEM_PROMPT
    )]
    for d in history_docs:
        if d.get("role") == "user":
            msgs.append(HumanMessage(content=d.get("text", "")))
        elif d.get("role") == "assistant":
            msgs.append(AIMessage(content=d.get("text", "")))
    msgs.append(HumanMessage(content=new_user_text))
    return msgs

_agent_graph = None

async def get_agent_graph():
    global _agent_graph
    if _agent_graph is not None:
        return _agent_graph

    model = init_chat_model(settings.GEMINI_MODEL, api_key=settings.GOOGLE_API_KEY)

    tools = []
    model_with_tools = model.bind_tools(tools)

    async def call_model(state: AgentState):
        resp = await model_with_tools.ainvoke(state["messages"])
        return {"messages": [resp]}

    builder = StateGraph(AgentState)
    builder.add_node("call_model", call_model)
    builder.add_edge(START, "call_model")

    _agent_graph = builder.compile()
    png_data = _agent_graph.get_graph().draw_mermaid_png()
    with open("graph_visualization.png", "wb") as f:
        f.write(png_data)
        
    return _agent_graph
