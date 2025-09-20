# [Workshop1-4] MCP LINE

This workshop shows how to run a **Model Context Protocol (MCP) server** for LINE using **Docker** and **mcp-proxy**. No custom Python server is needed—just configure your environment variables, build the container, and expose your endpoint.

---

## 🚀 Getting Started

### Option 1: Run in GitHub Codespaces (Recommended)

1. Click the **Code** button in this repo.
2. Select **Open with Codespaces → New Codespace**.
3. Open Terminal and change the path to this workshop:

   ```bash
   cd /workspaces/Basic-Agent-MCP/day_2/1_MCP/03_LineTool
    ````

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
   cd Basic-Agent-MCP/day_2/1_MCP/03_LineTool
   ```

2. Clone the LINE MCP server and build the Docker container:

   ```bash
   git clone https://github.com/line/line-bot-mcp-server.git
   docker build -t line/line-bot-mcp-server line-bot-mcp-server/.
   ```

---

## ⚙️ Environment Configuration

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` and set the following variables:

   ```text
   LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
   ```

---

## ▶️ Run with Docker Container

```bash
mcp-proxy \
  --host 0.0.0.0 \
  --port 4000 \
  --pass-environment \
  --allow-origin "*" \
  -- docker run -i --rm \
       --env-file .env \
       line/line-bot-mcp-server
```

> **Important:** This exposes a public port. Your MCP client should use the endpoint with `/sse` path:
> `http://YOUR_END_POINT/sse`

---

## ✅ Verify & Inspect

* **Local check (curl):**

```bash
curl -i http://localhost:4000/sse
```

* **MCP Inspector (optional):**
  Point it to your server’s URL (or Codespaces forwarded URL) to verify your MCP LINE server is working.

---

## 🛠 Troubleshooting

* **Port already in use**
  Change the `--port` value in your `mcp-proxy` command and restart.

* **Firewall / access issues**
  Ensure the port is reachable:

  * Codespaces → set port to **Public**
  * Local → allow inbound connections to `3000`

* **Environment variable issues**
  Make sure `LINE_CHANNEL_SECRET` are correctly set in `.env`.

---

## 📚 Reference

* LINE MCP server: [GitHub repo](https://github.com/line/line-bot-mcp-server)