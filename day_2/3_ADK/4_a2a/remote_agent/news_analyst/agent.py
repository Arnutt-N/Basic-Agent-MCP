from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
import pytz
from google.adk.a2a.utils.agent_to_a2a import to_a2a

def get_current_time():
    """คืนค่าเวลาปัจจุบันในโซนเวลา Bangkok (Asia/Bangkok)
    รูปแบบ: YYYY-MM-DD HH:MM:SS

    Returns:
        str: เวลาปัจจุบันในโซนเวลาไทย
    """
    tz = pytz.timezone("Asia/Bangkok")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# Agent ช่วยวิเคราะห์ข่าวและสรุปข่าวให้ผู้ใช้
news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="News analyst agent",
    instruction="""
    คุณเป็นผู้ช่วยที่สามารถวิเคราะห์บทความข่าวและสรุปข่าวให้กับผู้ใช้ได้
    เมื่อถูกถามเกี่ยวกับข่าว คุณควรใช้เครื่องมือ google_search เพื่อค้นหาข่าว
    หากผู้ใช้ถามข่าวโดยใช้เวลาสัมพัทธ์ คุณควรใช้เครื่องมือ get_current_time เพื่อรับเวลาปัจจุบันสำหรับใช้ในการค้นหา
    """,
    tools=[google_search, get_current_time],
)


skill = AgentSkill(
    id='get_exchange_rate',
    name='Currency Exchange Rates Tool',
    description='Helps with exchange values between various currencies',
    tags=['currency conversion', 'currency exchange'],
    examples=['What is exchange rate between USD and GBP?'],
)
Then as part of the AgentCard it will list the agent's skills and capabilities alongside additional details like input and output modes that the agent can handle:


# A2A Agent Card definition
agent_card = AgentCard(
    name='Currency Agent',
    description='Helps with exchange rates for currencies',
    url=f'http://{host}:{port}/',
    version='1.0.0',
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
)
a2a_app = to_a2a(news_analyst, port=8001)