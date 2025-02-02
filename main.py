import telebot
from telebot import types
import random

class TelegramBot():
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.kb = types.InlineKeyboardMarkup(row_width=2)
            self.btn = types.InlineKeyboardButton(text='no', callback_data='btn1')
            self.kb.add(self.btn)
            self.bot.send_message(message.chat.id, 'no', reply_markup=self.kb)

        @self.bot.callback_query_handler(func=lambda callback: callback.data)
        def call(callback):
          if callback.data == 'btn1':
            d = self.bot.send_message(callback.message.chat.id, 'Введите число')
            self.bot.register_next_step_handler(d, next)
            
        def next(message):
            a = random.randint(0, 9)
            if int(message.text) == a:
               self.bot.send_message(message.chat.id, f'Вы победили, число {a}')
            else:
               self.bot.send_message(message.chat.id, f'Вы проиграли, число {a}')
             

    def run(self):
        self.bot.polling()

TOKEN = 'TOKEN SYUDA'
bot = TelegramBot(TOKEN)
bot.run()