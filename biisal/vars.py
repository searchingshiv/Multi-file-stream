# (c) adarsh-goel (c) @biisal (c) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
DS_bot_name = "Silent Streamer" #This Extra Function Added By 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
DS_bot_username = "DS_FILE_2_LINK_BOT" #Add Bot Username Without '@'
silent_channel = "https://telegram.me/THE_SILENT_TEAMS" #Update Channel Link
silent_auto_grp = "https://t.me/+CZH0JaSwih44ZTM1" #Auto Filter Group Link

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', ''))
    API_HASH = str(getenv('API_HASH', ''))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6636524134:AAEdE7N4IzG-0Fjarvxb_L8Di8lsPVoxet8'))
    name = str(getenv('name', 'DSFile-To-Link'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10000'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001925180658'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001925180658'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1562935405").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'THE_DS_OFFICIAL'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here, Edited by 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'none')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    
