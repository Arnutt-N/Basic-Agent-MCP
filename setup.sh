git clone https://github.com/line/line-bot-mcp-server.git
cd line-bot-mcp-server
docker build -t line/line-bot-mcp-server .
pipx install mcp-proxy || uv tool install mcp-proxy