from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)
    auth_token = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class CreditCard(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    card_number = Column(String, nullable=False)
    balance = Column(Float, default=0.0)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), nullable=False)
    description = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())