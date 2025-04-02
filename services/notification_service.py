from aiogram import Bot

class NotificationService:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def send_transaction_notification(self, chat_id: int, transaction):
        message = (f"🔔 Yangi tranzaksiya:\n"
                   f"Miqdor: {transaction['amount']} {transaction['currency']}\n"
                   f"Sana: {transaction['date']}\n"
                   f"Izoh: {transaction['description']}")
        await self.bot.send_message(chat_id, message)