from telebot import types
from flask import request

from config import app, bot, secret


@app.route('/')
@app.route('/healthcheck')
def healthcheck():
    return '<h1>OK. Server still runing...</h1>'


@app.route('/' + secret, methods=['POST'])
def webhook():
    """
    Route для прослуховування вхідних запитів від телеграму.
    Використовується, якщо бот запущений через start_bot_weebook()
    :return:
    """
    update = types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200
