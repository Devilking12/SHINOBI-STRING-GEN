from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27383453"))
API_HASH = getenv("API_HASH", "4c246fb0c649477cc2e79b6a178ddfaa")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "8447127606"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://heistteam1:heistteam1@cluster0.24oegbu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "ITSZSHUKLA")
START_IMG = getenv("START_IMG", "https://files.catbox.moe/520y6h.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "MASTIWITHFRIENDSXD")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "SHIVANSH474")
