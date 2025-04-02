import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')

# Bank API Configuration
BANK_API_KEY = os.getenv('BANK_API_KEY')
BANK_API_ENDPOINT = os.getenv('BANK_API_ENDPOINT')

# Security Settings
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')