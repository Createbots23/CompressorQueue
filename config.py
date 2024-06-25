from decouple import config

try:
    APP_ID = config("APP_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()￼Enter
