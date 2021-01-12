import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

channels = [
    -1001200412225,

]

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")
