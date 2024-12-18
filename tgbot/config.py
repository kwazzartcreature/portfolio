import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://example.com/webhook")
WEBHOOK_PATH = "/webhook"
HOST = "0.0.0.0"
PORT = int(os.getenv("WEBAPP_PORT", 8000))
