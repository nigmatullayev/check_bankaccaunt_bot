import asyncio
from aiogram import Bot, Dispatcher
from config.settings import TELEGRAM_BOT_TOKEN
from bot.handlers import start_command, balance_command, transaction_history_command

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(balance_command, commands=['balance'])
    dp.register_message_handler(transaction_history_command, commands=['history'])

    await dp.start_polling()