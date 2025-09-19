# [Workshop1-2] MCP Inspector

This workshop helps participants inspect and debug MCP servers using the official MCP Inspector UI—no extra scaffolding. Just run one command and start exploring tools, prompts, and schemas exposed by any MCP server.

---

## 🚀 Getting Started

### Option 1: Run in GitHub Codespaces (Recommended)

1. Click the **Code** button in this repo.
2. Select **Open with Codespaces → New Codespace**.
3. Open Terminal and Change the path to this workshop
   ```bash
   cd /workspaces/Basic-Agent-MCP/day_2/1_MCP/02_DebugTool
   ```

---

### Option 2: Run Locally (Clone Repo)

Clone this repository:

   ```bash
   git clone https://github.com/ro-witthawin/Basic-Agent-MCP.git
   cd Basic-Agent-MCP/day_2/1_MCP/02_DebugTool
   ```

---

## ▶️ Run the Inspector:

```bash
npx -y @modelcontextprotocol/inspector
```

**Expected:** The Inspector will start and print a local URL. Open it in your browser (or it may auto-open)

---

## 🧭 Using MCP Inspector

Once the UI opens, you can:

* **Connect to an MCP server (HTTP/SSE/Streamable-HTTP):**
  Paste your server URL (e.g., a Codespaces-forwarded URL or localhost port).
* **Connect to a stdio-based server (advanced):**
  Use the Inspector’s “Run a command” option and enter the command that starts your stdio server.
* **Explore capabilities:**

  * Browse **tools** and try **invocations** interactively
  * View **schemas**, **resources**, and **prompts**
  * Inspect **requests/responses** for quick debugging

> For classroom flow: pair this with a simple MCP server workshop and have participants point Inspector at the server they just launched.

---

## 🧪 Quick Checks

* **Local health check (server-side):** If you’re testing against a local HTTP MCP server, verify it’s reachable:

  ```bash
  curl -i http://localhost:<PORT>/
  ```
* **Codespaces remote check:** Ensure the target MCP server port is **Public** and use the **Forwarded URL** in Inspector.&#x20;

---

## 🛠 Troubleshooting

* **`npx: command not found`**
  Install Node.js (which includes `npx`). On macOS:

  ```bash
  brew install node
  ```
* **Inspector opens but cannot connect to my server**

  * Confirm the server is actually running and listening on the URL/port you entered.
  * For Codespaces, mark the target port as **Public** and use the **Forwarded URL**.&#x20;
* **CORS / mixed content issues**
  If your server is HTTP and the Inspector page is HTTPS (or vice versa), align schemes or allow the origin in your server config.

---

## ✅ Goals

* Start the **official MCP Inspector** with one command.
* Learn to **connect** to MCP servers and **exercise tools** interactively.
* Use Inspector to **debug** schemas, payloads, and responses.

---

## 📝 Notes

* This workshop intentionally ships **no server code**—the focus is purely on the Inspector.
* Pair this session with another workshop (e.g., FastMCP server) for end-to-end practice: start a server, then inspect it here.