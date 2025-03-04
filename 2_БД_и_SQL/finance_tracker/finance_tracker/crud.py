# finance_tracker/crud.py
from sqlalchemy.orm import Session
from . import models
from sqlalchemy import and_
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

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

def update_transaction(db: Session, transaction_id: int, amount: float = None, type: str = None, category_id: int = None):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        return None

    if amount is not None:
        transaction.amount = amount
    if type is not None:
        transaction.type = type
    if category_id is not None:
        transaction.category_id = category_id

    db.commit()
    db.refresh(transaction)
    return transaction

def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        return False

    db.delete(transaction)
    db.commit()
    return True

def get_transactions_by_type(db: Session, user_id: int, transaction_type: str):
    return db.query(models.Transaction).filter(
        and_(
            models.Transaction.user_id == user_id,
            models.Transaction.type == transaction_type
        )
    ).all()

def get_transactions_sorted(db: Session, user_id: int, sort_by: str = "date", order: str = "asc"):
    query = db.query(models.Transaction).filter(models.Transaction.user_id == user_id)

    if sort_by == "date":
        if order == "asc":
            query = query.order_by(models.Transaction.date)
        else:
            query = query.order_by(desc(models.Transaction.date))
    elif sort_by == "amount":
        if order == "asc":
            query = query.order_by(models.Transaction.amount)
        else:
            query = query.order_by(desc(models.Transaction.amount))

    return query.all()

def create_user(db: Session, name: str, email: str):
    try:
        user = models.User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Ошибка при создании пользователя: {e}")
        return None