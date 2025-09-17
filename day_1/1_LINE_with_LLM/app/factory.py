# app/factory.py
from fastapi import FastAPI
from app.webhooks.line import router as line_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="LINE x Gemini x LangGraph",
        version="1.0.0",
    )

    # Routers
    app.include_router(line_router, prefix="/line", tags=["line"])

    return app
