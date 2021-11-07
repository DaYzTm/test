import os
import telebot
from flask import Flask, request

TOKEN = '2122255296:AAEMan6pedu1W54NxFeoRWX_A4etUoW2-H8'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)
