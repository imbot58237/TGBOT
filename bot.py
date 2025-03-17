import telebot

TOKEN = "7735251898:AAEq7Rq9ikpUIT25Gl8JKL4F8Bn7POB_hAY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🔥 হ্যালো! আমি তোমার টেলিগ্রাম বট!")

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    bot.send_message(message.chat.id, f"তুই বললি: {message.text}")

print("🤖 Bot is running...")
bot.polling()
