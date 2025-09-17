# app/db/repositories.py
from typing import Any, Literal, List
from bson import ObjectId
from datetime import datetime

from app.db.mongo import get_db
from app.utils.time import now_utc

async def upsert_user_profile(
    uid: str,
    *,
    display_name: str | None,
    picture_url: str | None,
    status_message: str | None,
    language: str | None,
    last_seen_at: datetime | None = None,
    channel: str = "line",
    raw_profile: dict | None = None,
) -> None:
    """Insert or update a user's LINE profile + last_seen_at."""
    db = get_db()
    now = now_utc()
    update = {
        "$setOnInsert": {
            "uid": uid,
            "created_at": now,
            "channel": channel,
        },
        "$set": {
            "display_name": display_name,
            "picture_url": picture_url,
            "status_message": status_message,
            "language": language,
            "last_seen_at": last_seen_at or now,
            "updated_at": now,
        },
    }
    if raw_profile is not None:
        update["$set"]["meta"] = {"line_profile_raw": raw_profile}

    await db["users"].update_one({"uid": uid}, update, upsert=True)

async def save_message(
    uid: str,
    role: Literal["user", "assistant", "system"],
    text: str,
    ts=None,
    channel: str = "line",
    meta: dict[str, Any] | None = None,
) -> str:
    db = get_db()
    doc = {
        "uid": uid,
        "role": role,
        "text": text,
        "ts": ts or now_utc(),
        "channel": channel,
        "meta": meta or {},
    }
    res = await db["messages"].insert_one(doc)
    return str(res.inserted_id)

async def get_last_messages(uid: str, n_latest: int) -> List[dict]:
    db = get_db()
    cursor = db["messages"].find({"uid": uid}).sort("ts", 1)
    docs = await cursor.to_list(length=1000)
    return docs[-n_latest:] if len(docs) > n_latest else docs
