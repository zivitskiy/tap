from flask import Flask, render_template, request
import telebot
from config import bot_token, chat_id

app = Flask(__name__)

bot = telebot.TeleBot(bot_token)


@app.route('/')
def home():
    if request.headers.getlist("X-Forwarded-For"):
        visitor_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        visitor_ip = request.remote_addr

    print(visitor_ip)

    # Send IP address to Telegram
    bot.send_message(chat_id, f"New visitor IP: {visitor_ip}")

    return render_template('index.html', visitor_ip=visitor_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
