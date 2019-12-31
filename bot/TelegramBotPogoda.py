import telebot
import pyowm
from telebot import apihelper

owm = pyowm.OWM('d41a733192602688c50263e6365382f5', language="ru")
bot = telebot.TeleBot("957572159:AAGW6A3my3CI9k6bh4G4syoP2dCxfDLRR8M")



@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answer = "Повелитель, в городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "А температура " + str(temp) + "\n"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
