import os

from dotenv import load_dotenv
import telebot
from flask import Flask

load_dotenv()
token = os.getenv("token")
secret = os.getenv("secret")
port = os.getenv("port")


bot = telebot.TeleBot(token, parse_mode=None)

app = Flask(__name__)
