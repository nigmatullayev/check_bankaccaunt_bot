from sqlalchemy.orm import Session
from .models import User, CreditCard, Transaction
from cryptography.fernet import Fernet

class DatabaseManager:
    def __init__(self, session: Session, encryption_key: str):
        self.session = session
        self.cipher_suite = Fernet(encryption_key.encode())

    def create_user(self, telegram_id: str, auth_token: str):
        encrypted_token = self.cipher_suite.encrypt(auth_token.encode()).decode()
        user = User(telegram_id=telegram_id, auth_token=encrypted_token)
        self.session.add(user)
        self.session.commit()
        return user

    def save_transaction(self, user_id: int, amount: float, currency: str, description: str):
        transaction = Transaction(
            user_id=user_id,
            amount=amount,
            currency=currency,
            description=description
        )
        self.session.add(transaction)
        self.session.commit()
        return transaction