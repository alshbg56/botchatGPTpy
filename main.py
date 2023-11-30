import telebot
from telebot import types
from server import server
from chatgpt import chatgpt

bot = telebot.TeleBot("6951775983:AAHeTURJvlkz83mLU2lW4fGwAEdb-Agrn9k")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  if message.chat.type == "private":
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id,"مرحبا بك في بوت ChatGPT",reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  msgid = bot.reply_to(message, "...").id
  x = chatgpt(message.text)
  bot.edit_message_text(x, message.chat.id, msgid)

server()
bot.infinity_polling()
