# MCP GoogleMap
## Initial Terminal Path
```cd /workspaces/Basic-Agent-MCP/day_2/1_MCP/02_GoogleMapTool```

## Install `mcp-proxy`
```pipx install mcp-proxy || uv tool install mcp-proxy```

## Setup Variable
```cp .env.example .env```

Setup your variable
`GOOGLE_MAPS_API_KEY` 

## Run with Docker Container
```
mcp-proxy \
  --host 0.0.0.0 \
  --port 8080 \
  --pass-environment \
  --allow-origin "*" \
  -- docker run -i --rm \
       --env-file .env \
       mcp/google-maps
```

!!! Public Port !!!

Finally this is your endpoint. Don't forget add path `/sse` to your endpoint
`http://YOUR_END_POINT>/sse`

## Reference
https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps