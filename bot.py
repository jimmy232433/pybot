import telebot 
bot = telebot.TeleBot("1389463263:AAEbPIqqWJSHLaeFBoPYofOVfV-hKg_wmxg")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message_text == "/start":
        bot.Send_messagge(message.chat.id, "ciao")
 bot.polling()

