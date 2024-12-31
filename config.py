from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "28916577"
# -------------------------------------------------------------
API_HASH = "24f26bdbcca723053f2bd09ad524f904"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6961211249"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/INNOCENTBOY2926/INNOCENT-CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "THE_FUCKER_BOTS_2926"
UPDATE_CHNL = "THE_FUCKING_BOT_2926"
OWNER_USERNAME = "its_innocent_boy_2926"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
