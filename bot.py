import telebot 
bot = telebot.TeleBot(token)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message_text == "/start":
        bot.Send_messagge(message.chat.id, "ciao")
        

