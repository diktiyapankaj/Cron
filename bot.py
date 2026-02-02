import time
import requests
from telegram import Bot

BOT_TOKEN = "8397089498:AAFPE2NhTfVM22XdkOGOQRFHejd0yxrggj8"
CHAT_ID = "1139295957"
API_URL = "https://example.com/api"

bot = Bot(token=BOT_TOKEN)

while True:
    try:
        r = requests.get(API_URL, timeout=10)
        text = r.text[:4000]  # telegram limit safe
    except Exception as e:
        text = str(e)

    bot.send_message(chat_id=CHAT_ID, text=text)
    time.sleep(60)
