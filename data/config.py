import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

channels = []

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")
