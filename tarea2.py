import os
import telebot
from telebot.types import Message

bot=telebot.TeleBot('1897077344:AAED_6T16Qu9FZETiviuC3Z6nCKgjBMhV1Y')
@bot.message_handler(commands=['dolar'])

def precio_dolar(mensaje):
    bot.reply_to(mensaje,"El precio del dolar es de 23.8486 Lempiras")

@bot.message_handler(commands=['euro'])
def precio_euro(mensaje):
    bot.reply_to(mensaje,"El precio del euro es de 29.8486 Lempiras")

@bot.message_handler(commands=['oro'])
def precio_oro(mensaje):
    bot.reply_to(mensaje,"El precio del oro es de 120 Lempiras Kg")

@bot.message_handler(commands=['cafe'])
def precio_cafe(mensaje):
    bot.reply_to(mensaje,"El precio del cafe es de 800 Lempiras el quintal")

bot.polling()