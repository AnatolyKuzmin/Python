# finance_tracker/crud.py
from sqlalchemy.orm import Session
from . import models
from sqlalchemy import and_
from datetime import datetime

def create_user(db: Session, name: str, email: str):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_transactions(db: Session, user_id: int):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()

def add_transaction(db: Session, user_id: int, category_id: int, amount: float, transaction_type: str):
    transaction = models.Transaction(
        amount=amount,
        type=transaction_type,
        user_id=user_id,
        category_id=category_id
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def create_category(db: Session, name: str):
    category = models.Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(models.Category.name == name).first()

def get_transactions_by_date(db: Session, user_id: int, start_date: datetime, end_date: datetime):
    return db.query(models.Transaction).filter(
        and_(
            models.Transaction.user_id == user_id,
            models.Transaction.date >= start_date,
            models.Transaction.date <= end_date
        )
    ).all()

def get_transactions_by_category(db: Session, user_id: int, category_id: int):
    return db.query(models.Transaction).filter(
        and_(
            models.Transaction.user_id == user_id,
            models.Transaction.category_id == category_id
        )
    ).all()