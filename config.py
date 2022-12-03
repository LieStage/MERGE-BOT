import os


class Config(object):
    
    API_HASH = os.environ.get("API_HASH","3eba5d471162181b8a3f7f5c0a23c307")
    PORT = os.environ.get("PORT","8080")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5576425861:AAHcR9zMJaY1h6WZ8dZ1d8Cu6eHEGOs4JMc")
    TELEGRAM_API = os.environ.get("TELEGRAM_API","4682685")
    OWNER = os.environ.get("OWNER","945284066")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","FLIGHER")
    PASSWORD = os.environ.get("PASSWORD","1245")
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://video:merge@cluster0.km7eaiw.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL","-1001655909201")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
    
