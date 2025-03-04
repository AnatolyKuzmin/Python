# finance_tracker/crud.py
from sqlalchemy.orm import Session
from . import models

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