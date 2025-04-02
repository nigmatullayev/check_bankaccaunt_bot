import requests
from config.settings import BANK_API_ENDPOINT, BANK_API_KEY

class BankAPIService:
    @staticmethod
    def get_card_balance(card_token: str):
        headers = {
            'Authorization': f'Bearer {BANK_API_KEY}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{BANK_API_ENDPOINT}/balance',
                                headers=headers,
                                params={'token': card_token})
        return response.json()

    @staticmethod
    def get_recent_transactions(card_token: str, limit: int = 10):
        headers = {
            'Authorization': f'Bearer {BANK_API_KEY}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{BANK_API_ENDPOINT}/transactions',
                                headers=headers,
                                params={'token': card_token, 'limit': limit})
        return response.json()