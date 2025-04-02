from aiogram import Dispatcher, types
from services.bank_api import BankAPIService
from services.notification_service import NotificationService
from .keyboards import get_main_keyboard

async def start_command(message: types.Message):
    await message.reply(
        "Kredit kartani kuzatish botiga xush kelibsiz! 💳\n"
        "Kartangizni ulash uchun /connect buyrug'ini ishlating.",
        reply_markup=get_main_keyboard()
    )

async def balance_command(message: types.Message):
    # Authenticate and fetch balance
    balance = BankAPIService.get_card_balance(user_token)
    await message.reply(f"Hozirgi balans: {balance['amount']} {balance['currency']}")

async def transaction_history_command(message: types.Message):
    transactions = BankAPIService.get_recent_transactions(user_token)
    response = "Oxirgi tranzaksiyalar:\n"
    for transaction in transactions:
        response += (f"• {transaction['amount']} {transaction['currency']} "
                     f"({transaction['date']}): {transaction['description']}\n")
    await message.reply(response)