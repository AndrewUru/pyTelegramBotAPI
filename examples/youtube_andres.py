import requests
import os

#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '<6743646945:AAHBraiR9eRwpQQjg-pc6GsXflYTaw21YI8>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

# Token de API de Telegram
token = "6743646945:AAHBraiR9eRwpQQjg-pc6GsXflYTaw21YI8"

# ID del grupo de Telegram
chat_id = "5802470376"

# Código modificado

def like_video(url):
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.post("https://www.googleapis.com/youtube/v3/videos/like", headers=headers, params={"id": url})
    return response.status_code == 200

def take_screenshot(url):
    browser = webdriver.Chrome()
    browser.get(url)
    screenshot = browser.save_screenshot("screenshot.png")
    return screenshot

def share_screenshot(screenshot):
    with open("screenshot.png", "rb") as f:
        bot.send_photo(chat_id, f)

def main():
    message = bot.get_updates()[0]
    url = message.text
    if like_video(url):
        screenshot = take_screenshot(url)
        share_screenshot(screenshot)

if __name__ == "__main__":
    main()
