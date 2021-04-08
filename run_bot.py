from pyngrok import ngrok

from config import app, bot, secret, port
import bot_handlers
import app_routes


def start_bot_getupdates():
    bot.remove_webhook()
    bot.infinity_polling(timeout=60, long_polling_timeout=100)


def start_bot_weebook_ngrok():
    bot.remove_webhook()
    ngrok_conn = ngrok.connect(port)
    http_url = ngrok_conn.public_url
    https_url = http_url.replace('http://', 'https://')
    bot.set_webhook(url=https_url + '/' + secret)
    print(f'------------- ONLY FOR TESTS (USING Webhook and pyngrok) -------------\n'
          f'http_url = {http_url}\nhttps_url={https_url}\n')
    app.run(debug=True)


if __name__ == '__main__':
    start_bot_weebook_ngrok()   # or use start_bot_getupdates()
