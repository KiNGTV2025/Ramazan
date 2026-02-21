
import os
import requests
from ai_generator import generate_message
from datetime import datetime

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def run():
    now = datetime.now().hour

    if now < 12:
        message = generate_message("Sahur")
    else:
        message = generate_message("İftar")

    send_telegram(message)

if __name__ == "__main__":
    run()
