# finance_tracker/utils.py
from sqlalchemy.orm import Session
from . import models

def calculate_balance(db: Session, user_id: int):
    incomes = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == "income"
    ).scalar() or 0

    expenses = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == "expense"
    ).scalar() or 0

    return incomes - expenses