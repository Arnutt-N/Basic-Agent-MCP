# [Workshop1-1] Custom FastMCP Server

This workshop shows how to build and run a **Model Context Protocol (MCP) server** using **fastmcp** in pure Python. No proxy needed—just configure a port, run `python main.py`, and connect your MCP client.

---

## 🚀 Getting Started

### Option 1: Run in GitHub Codespaces (Recommended)

1. Click the **Code** button in this repo.
2. Select **Open with Codespaces → New Codespace**.
3. Open Terminal and Change the path to this workshop
   ```bash
   cd /workspaces/Basic-Agent-MCP/day_2/1_MCP/01_FastMCP
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### Option 2: Run Locally (Clone Repo)

1. Clone this repository:

   ```bash
   git clone https://github.com/ro-witthawin/Basic-Agent-MCP.git
   cd Basic-Agent-MCP/day_2/1_MCP/01_FastMCP
   ```

2. Create and activate a Python environment (Python 3.8+ required):

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Environment Configuration

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` and set the following values:

    * `MCP_PORT` → Port for the FastMCP HTTP server to listen (Default 7000)

---

## ▶️ Run the Server

```bash
python main.py
```

**Expected:** The console logs show your MCP server is listening on `MCP_PORT`.
Example:

```
FastMCP server started on http://0.0.0.0:8080
```

> If you’re in Codespaces, use the **Ports** tab to expose the port publicly if an external client needs to reach it.

---

## ✅ Verify & Inspect

* **Local check (curl):**

  ```bash
  curl -i http://localhost:$MCP_PORT/
  ```

  Your server may return a simple health/hello response (optional based on your `main.py`).

* **MCP Inspector (optional):**
  If you use the MCP Inspector locally, point it to your server’s URL (or Codespaces forwarded URL) that matches `MCP_PORT`.

---

## 🛠 Troubleshooting

* **Port already in use**
  Change `MCP_PORT` in `.env` (e.g., 8081) and restart:

  ```bash
  MCP_PORT=8081 python main.py
  ```
* **Firewall / access issues**
  Ensure the port is reachable:

  * Codespaces → set port to **Public**
  * Local → allow inbound connections to `MCP_PORT`
* **Virtualenv not activated**
  Dependencies missing? Activate your venv or reinstall:

  ```bash
  pip install -r requirements.txt
  ```

---

## 📝 Notes

* This workshop focuses **only** on standing up an MCP server with **fastmcp**.
* Clients (IDE plugins, agents, or tools) can connect to your server using the URL/port you expose.

---

## 📚 Tech Stack

* **Python 3.10+** (recommended)
* **fastmcp** for MCP server utilities
* **dotenv** for environment configuration
* (Optional) **FastAPI**/**Starlette** style patterns if you extend HTTP endpoints
