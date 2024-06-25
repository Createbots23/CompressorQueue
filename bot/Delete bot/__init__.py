import asyncio
import glob
import inspect
import io
import itertools
import json
import math
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import traceback
from datetime import datetime as dt
from logging import DEBUG, INFO, basicConfig, getLogger, warning
from pathlib import Path

import aiohttp
import psutil
import pymediainfo
import requests
from html_telegraph_poster import TelegraphPoster
from telethon import Button, TelegramClient, errors, events, functions, types
from telethon.sessions import StringSession
from telethon.utils import pack_bot_file_id

from .config import *
from aiohttp import web
from plugins.web_support import web_server
import pyromod

basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger(__name__)


try:
    bot = TelegramClient(None, APP_ID, API_HASH)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()


async def startup():
    for x in OWNER.split():
        app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()
        try:
            await bot.send_message(int(x), "**Bot is Successfully Deployed**")
        except BaseException:
            pass
               please check the information you give
            
Bot().run()￼Enter
