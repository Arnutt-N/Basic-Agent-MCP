# MCP LINE
## Initial Terminal Path
```cd /workspaces/Basic-Agent-MCP/day_2/1_MCP/03_LineTool```

## Install `mcp-proxy`
```pipx install mcp-proxy || uv tool install mcp-proxy```

## Clone LINE-bot-mcp-server & Build container 
```
git clone https://github.com/line/line-bot-mcp-server.git
docker build -t line/line-bot-mcp-server line-bot-mcp-server/.
```

## Setup Variable
```cp .env.example .env```

`GOOGLE_MAPS_API_KEY` 
`LINE_CHANNEL_SECRET`

```
mcp-proxy \
  --host 0.0.0.0 \
  --port 3000 \
  --pass-environment \
  --allow-origin "*" \
  -- docker run -i --rm \
       --env-file .env \
       line/line-bot-mcp-server
```

!!! Public Port !!!

Finally this is your endpoint. Don't forget add path `/sse` to your endpoint
`http://YOUR_END_POINT>/sse`

## Reference
https://github.com/line/line-bot-mcp-server