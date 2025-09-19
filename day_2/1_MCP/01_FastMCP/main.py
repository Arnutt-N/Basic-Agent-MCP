from fastmcp import FastMCP
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Literal

import anyio

mcp = FastMCP(name="AsyncDemo")

# Input schema
class TimeQueryInput(BaseModel):
    query: str = Field(
        description='Specify the time keyword: "today", "now", "yesterday", "tomorrow"'
    )
    
# Tool definition
@mcp.tool
def get_time(query: str):
    """Returns the date or datetime for 'today', 'now', 'yesterday', or 'tomorrow'."""
    now = datetime.now()
    query_lower = query.lower()

    if query_lower == "today":
        return now.strftime("%Y-%m-%d")
    elif query_lower == "now":
        return now.strftime("%Y-%m-%d %H:%M:%S")
    elif query_lower == "yesterday":
        return (now - timedelta(days=1)).strftime("%Y-%m-%d")
    elif query_lower == "tomorrow":
        return (now + timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        return {"error": f"Unknown time query '{query}'. Use 'today', 'now', 'yesterday', or 'tomorrow'."}

if __name__ == "__main__":
    mcp.run()