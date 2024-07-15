import os
from dotenv import load_dotenv
import telebot
import requests


load_dotenv()

HORO_TOKEN = os.environ.get('HORO_TOKEN')
bot = telebot.TeleBot(HORO_TOKEN)


def get_daily_horoscope(sign: str, day: str) -> dict:
   """
       Get daily horoscope for a zodiac sign.
       Keyword arguments:
       sign:str - Zodiac sign
       day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
       Return:dict - JSON data
   """
   url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
   params = {"sign": sign, "day": day}
   response = requests.get(url, params)


   return response.json()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
   bot.reply_to(message, "Hello fellow enthusiastic Horoscoper!\n\nLet's manifest and control our destiny!!\n\nTo begin type /horoscope")


@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
   text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
   sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
   bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
   sign = message.text
   text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
   sent_msg = bot.send_message(
       message.chat.id, text, parse_mode="Markdown")
   bot.register_next_step_handler(
       sent_msg, fetch_horoscope, sign.capitalize())


def fetch_horoscope(message, sign):
   """
       {
           "data":{
               "date": "Dec 15, 2022",
               "horoscope_data": "Lie low during the day and try not to get caught up in the frivolous verbiage that dominates the waking hours. After sundown, feel free to speak your mind. You may notice that there is a sober tone and restrictive sensation today that leaves you feeling like you will never be able to break free from your current situation. Don't get caught in this negative mindset."
           },
           "status": 200,
           "success": true
           }
   """
   day = message.text
   horoscope = get_daily_horoscope(sign, day)
   data = horoscope["data"]
   horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
   bot.send_message(message.chat.id, "Here's your horoscope!")
   bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


# @bot.message_handler(func=lambda message: True)
# def reply_back(message):
   # bot.send_message(chat_id=message.chat.id, text="I am not sure what you are asking for. Please type /horoscope to get your daily horoscope.")


bot.infinity_polling()