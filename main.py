import updater

import job_queue
import config
import telebot
import requests
from my_parser import parse
from bs4 import BeautifulSoup as BS


bot = telebot.TeleBot(config.token)
job_queue = updater.job_queue
r = requests.get('https://sinoptik.ua/погода-санкт-петербург')
html = BS(r.content, 'html.parser')

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    min_text = el.select('.wDescription .description')[0].text
    t_test = el.select('.wDescription .description')[0].text

response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
data = response.json()
btc_price = f"Биткоин: {round(data.get('btc_usd').get('last'), 2)}$"

@bot.message_handler(commands=['start', 'help'])
def main(updater,message):
    bot.send_message(
        message.chat.id, 'Погода на сегодня:' + t_min + ', ' + t_max + '\n' + min_text + '\n' + 'Доллар: ' + parse() + '₽' + '\n' + btc_price)
    job_queue.run_repeating(main, interval=10, first=0)
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

