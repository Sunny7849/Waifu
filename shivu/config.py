class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org/apps
    OWNER_ID = "8156600797"
    sudo_users = ("7349660966", "8156600797")  # Tuple me proper format
    GROUP_ID = -1002372914024
    TOKEN = "7539465396:AAFT5I6oK0wRJHSFNaAUMosQ4uFm2pHa7_c"
    
    mongo_url = "mongodb+srv://arzuquine:TGDARK11798@madarauzumaki.22wjzeb.mongodb.net/?retryWrites=true&w=majority"

    PHOTO_URL = [
        "https://graph.org/file/90344336f0da2961141a8-9129c1a27bb0bf675f.jpg",
        "https://graph.org/file/abc123example.jpg"
    ]

    SUPPORT_CHAT = "https://t.me/Anime_Circle_Club"
    UPDATE_CHAT = "https://t.me/+vDcCB_w1fxw1YTll"
    BOT_USERNAME = "Daddy_Madara_WaifuBot"
    CHARA_CHANNEL_ID = "-1002674487477"  # <-- yeh updated GC ID hai

    api_id = 28159105
    api_hash = "a0936ddf210a7e091e19947c7dc70c91"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
