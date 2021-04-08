import http.client
import telebot

from config import token, secret, port


conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ip_address_bytes = conn.getresponse().read()
ip_address = ip_address_bytes.decode("utf-8")

bot = telebot.TeleBot(token, parse_mode=None)

bot.remove_webhook()
webhook_url = f'{ip_address}:{port}/{secret}'
bot.set_webhook(webhook_url)

print(f'Webhook sucessfully set at url : {webhook_url}')
