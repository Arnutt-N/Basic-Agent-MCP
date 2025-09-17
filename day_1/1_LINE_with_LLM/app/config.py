# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

system_prompt = """
    You are a helpful assistant. Use tools when helpful. Reply concisely in the user's language.
"""

class Settings(BaseSettings):
    LINE_CHANNEL_SECRET: str
    LINE_CHANNEL_ACCESS_TOKEN: str
    GEMINI_MODEL: str = "google_genai:gemini-2.0-flash"
    GOOGLE_API_KEY: str | None = None
    
    SYSTEM_PROMPT: str = system_prompt

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()

