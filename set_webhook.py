import http.client
import telebot

from config import token, secret, port


conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ip_address_bytes = conn.getresponse().read()
ip_address = ip_address_bytes.decode("utf-8")

bot = telebot.TeleBot(token, parse_mode=None)

bot.remove_webhook()
bot.set_webhook(f'{ip_address}:{port}/{secret}')
