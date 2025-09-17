# app/db/schemas.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, Literal, Optional

class MessageIn(BaseModel):
    uid: str
    role: Literal["user", "assistant", "system", "tool"]
    text: str
    ts: datetime
    channel: str = "line"
    meta: dict[str, Any] | None = None

class MessageOut(BaseModel):
    id: str = Field(alias="_id")
    uid: str
    role: Literal["user", "assistant", "system", "tool"]
    text: str
    ts: datetime
    channel: str
    meta: dict[str, Any] | None = None

class UserIn(BaseModel):
    uid: str
    display_name: Optional[str] = None
    picture_url: Optional[str] = None
    status_message: Optional[str] = None
    language: Optional[str] = None
    last_seen_at: datetime
    channel: str = "line"