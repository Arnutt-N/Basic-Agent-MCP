# [Workshop1] LINE Webhook Chatbot with Gemini

This project demonstrates how to build a **LINE chatbot** powered by **Google Gemini (Generative AI)** using Python.
You can run it locally (by cloning this repo) or directly in **GitHub Codespaces**.

---

## 🚀 Getting Started

### Option 1: Run in GitHub Codespaces (Recommended)

1. Click the **Code** button in this repo.
2. Select **Open with Codespaces → New Codespace**.
3. Open Terminal and Change the path to this workshop
    ```bash
    cd /workspaces/Basic-Agent-MCP/day_1/1_LINE_with_LLM
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
   cd Basic-Agent-MCP
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

   * `GOOGLE_API_KEY` → Your Google Generative AI (Gemini) API key
   * `LINE_CHANNEL_SECRET` → Your LINE bot channel secret
   * `LINE_CHANNEL_ACCESS_TOKEN` → Your LINE bot channel access token

---

## ▶️ Running the Chatbot

Start the webhook server:

```bash
python main.py
```

## 🌐 Exposing Your Server to LINE

LINE requires a **publicly accessible HTTPS endpoint**. You have two options:

### 🔹 Option A: Codespaces Port Forwarding

1. In Codespaces, when you run:

   ```bash
   python main.py
   ```

   the app will start (default: `http://localhost:8000`).

2. Go to **Ports tab** in your Codespace (usually bottom panel).

3. Find port **8000**, right-click → **Make Public**.

4. Copy the **Forwarded URL** (looks like `https://xxxx-8000.app.github.dev`).

👉 Use this as your webhook endpoint:

```
https://xxxx-8000.app.github.dev/line/webhook
```

---

### 🔹 Option B: Ngrok (Local Development)

1. Start your app:

   ```bash
   python main.py
   ```

2. In another terminal, run ngrok:

   ```bash
   ngrok http 8000
   ```

3. Copy the generated HTTPS URL and set it as your LINE webhook endpoint:

```
https://<your-ngrok-id>.ngrok.io/line/webhook
```


Set your **LINE Webhook URL** in the LINE Developer Console to:

```
https://YOUR_ENDPOINT/line/webhook
```

---

## 📌 Notes

* Ensure your environment is running on **publicly accessible URL** (ngrok or Codespaces public port).
* Webhook path must end with `/line/webhook`.
* The chatbot flow:

  1. User sends a message to LINE bot.
  2. Webhook forwards to this server.
  3. Gemini processes the input and generates a response.
  4. The bot replies back to the user.

---

## 📚 Tech Stack

* **Python 3.8+**
* **FastAPI** for webhook handling
* **LINE Messaging API**
* **Google Gemini (Generative AI)**