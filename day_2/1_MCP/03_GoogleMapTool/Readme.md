# [Workshop1-3] MCP GoogleMap

This workshop shows how to run a **Model Context Protocol (MCP) server** for Google Maps using **Docker** and **mcp-proxy**. No custom Python server is needed—just configure your API key, run the Docker container, and expose your endpoint.

---

## 🚀 Getting Started

### Option 1: Run in GitHub Codespaces (Recommended)

1. Click the **Code** button in this repo.
2. Select **Open with Codespaces → New Codespace**.
3. Open Terminal and change the path to this workshop:

   ```bash
   cd /workspaces/Basic-Agent-MCP/day_2/1_MCP/03_GoogleMapTool
    ```

4. Install `mcp-proxy`:

   ```bash
   pipx install mcp-proxy
   # or
   uv tool install mcp-proxy
   ```

---

### Option 2: Run Locally (Clone Repo)

1. Clone this repository:

   ```bash
   git clone https://github.com/ro-witthawin/Basic-Agent-MCP.git
   cd Basic-Agent-MCP/day_2/1_MCP/03_GoogleMapTool
   ```

2. Install `mcp-proxy` as above.

---

## ⚙️ Environment Configuration

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` and set your Google Maps API key:

   ```bash
   GOOGLE_MAPS_API_KEY=YOUR_API_KEY
   ```

---

## ▶️ Run with Docker Container

```bash
mcp-proxy \
  --host 0.0.0.0 \
  --port 3000 \
  --pass-environment \
  --allow-origin "*" \
  -- docker run -i --rm \
       --env-file .env \
       mcp/google-maps
```

> **Important:** This exposes a public port. Your MCP client should use the endpoint with `/sse` path:
> `http://YOUR_END_POINT/sse`

---

## ✅ Verify & Inspect

* **Local check (curl):**

```bash
curl -i http://localhost:3000/sse
```

* **MCP Inspector (optional):**
  Point it to your server’s URL (or Codespaces forwarded URL) to verify your MCP GoogleMap server is working.

---

## 🛠 Troubleshooting

* **Port already in use**
  Change the `--port` value in your `mcp-proxy` command and restart.

* **Firewall / access issues**
  Ensure the port is reachable:

  * Codespaces → set port to **Public**
  * Local → allow inbound connections to `3000`

* **Environment variable issues**
  Make sure `GOOGLE_MAPS_API_KEY` is correctly set in `.env`.

---

## 📚 Reference

* MCP Google Maps server: [GitHub repo](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps)