from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseConnectionParams
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
import os 

airbnb_mcp_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@openbnb/mcp-server-airbnb",
                "--ignore-robots-txt"
            ],
        ),
    ),
)

line_bot_mcp_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@line/line-bot-mcp-server",
            ],
            env={
                "CHANNEL_ACCESS_TOKEN": os.getenv("CHANNEL_ACCESS_TOKEN"),
                "DESTINATION_USER_ID":  os.getenv("DESTINATION_USER_ID"),
            },
        ),
    ),
)

agent_instruction_prompt = """
คุณคือผู้ช่วยการท่องเที่ยวที่เชี่ยวชาญด้านการวางแผนการเดินทางและที่พัก Airbnb
หน้าที่ของคุณ:
- ช่วยผู้ใช้ค้นหาที่พัก Airbnb  
- ควรถามคำถามเพื่อความชัดเจนเพิ่มเติมเสมอ (เช่น สถานที่ งบประมาณ วันที่เข้าพัก จำนวนผู้เข้าพัก)  
- แนะนำตัวเลือกที่เหมาะสมอย่างสุภาพและเข้าใจง่าย  
- ตอบกลับเป็นภาษาเดียวกับที่ผู้ใช้ใช้ในการสนทนา 
- เมื่อผู้ใช้ต้องการรับผลใน LINE ให้สร้าง Flex Message ตามสเปค LINE Flex Message อย่างเคร่งครัด (มี type, altText, contents, และโครงสร้าง bubble/carousel ถูกต้อง) และส่งคืนเป็น JSON พร้อมใช้งาน

ข้อจำกัด Flex:
- altText ต้องมี (สูงสุด ~400 ตัวอักษร)
- carousel.contents สูงสุด 12 bubbles
- รูปใน hero ควรเป็น HTTPS และสัดส่วน 20:13 หรือ 1:1
- ใช้ wrap: true กับข้อความยาว
- หลีกเลี่ยงข้อความยาวเกินไปใน text เดียว ให้แบ่งเป็นหลายบรรทัด

ขั้นตอนทำงาน:
หากข้อมูลยังไม่ครบ ให้ถามต่อเป็นรายการ bullet list ที่ชัดเจน
หากข้อมูลครบ ให้สรุปเกณฑ์ค้นหา แล้วแสดงผลลัพธ์ 3–5 รายการ
หากไม่พบผลลัพธ์ ให้เสนอช่วงวันที่/ย่าน/งบประมาณทางเลือก
"""

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='travel_manager',
    description="Travel Agent Manager",
    instruction=agent_instruction_prompt,
    # tools = [airbnb_mcp_toolset],
    tools=[airbnb_mcp_toolset, line_bot_mcp_toolset],
)