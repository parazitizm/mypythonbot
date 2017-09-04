# пишу бота потому что хочу
"""
?
еще одно описание ?
?
"""
import telebot
valera = '394246782:AAGeErCJa9wLeyxbP-tQf8SQXiQCS7PoI8Y'
bot = telebot.TeleBot(valera)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('выбрать товар')
    user_markup.row('работа')
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "выбрать товар":
        bot.send_message(message.from_user.id, "соли миксы")
    if message.text == "работа":
        bot.send_message(message.from_user.id, "залог в 5000 рублей")

bot.polling(none_stop=True)
