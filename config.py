from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27613077"))
API_HASH = getenv("API_HASH", "19dccde5b307a489ec9ded3a8a558e34")
BOT_TOKEN = getenv("BOT_TOKEN", "8235842848:AAHWduszLN8fTgmKAYGO9xFBx2MchguLmq8")

OWNER_ID = int(getenv("OWNER_ID", "8447127606"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://heistteam1:heistteam1@cluster0.24oegbu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "Heist_x_Team")
START_IMG = getenv("START_IMG", "https://files.catbox.moe/520y6h.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Heist_Bots")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "Heist_x_Team")
