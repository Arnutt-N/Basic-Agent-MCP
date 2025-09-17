# app/services/langgraph.py
from __future__ import annotations
import json, time
from typing import Dict, List, Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, AIMessage, SystemMessage, BaseMessage
from langchain_core.messages import ToolMessage
from langchain_core.tools import BaseTool

from app.config import settings

# NEW: the graph state explicitly includes uid
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    uid: str

def build_prompt(new_user_text: str, history_docs: list[dict]=[]) -> List[BaseMessage]:
    msgs: List[BaseMessage] = [SystemMessage(
        content=settings.SYSTEM_PROMPT
    )]
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
        return {"messages": [resp]}  # uid is preserved automatically

    builder = StateGraph(AgentState)  # ← use our custom state
    builder.add_node("call_model", call_model)
    builder.add_edge(START, "call_model")

    _agent_graph = builder.compile()
    png_data = _agent_graph.get_graph().draw_mermaid_png()
    with open("graph_visualization.png", "wb") as f:
        f.write(png_data)
        
    return _agent_graph
