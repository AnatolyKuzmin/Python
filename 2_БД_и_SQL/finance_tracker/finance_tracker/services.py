# finance_tracker/services.py
from . import crud
from .database import get_db

def add_transaction_to_user(user_id: int, category_id: int, amount: float, transaction_type: str):
    db = next(get_db())
    return crud.add_transaction(db, user_id=user_id, category_id=category_id, amount=amount, transaction_type=transaction_type)

def get_user_balance(user_id: int):
    db = next(get_db())
    incomes = crud.get_user_incomes(db, user_id)
    expenses = crud.get_user_expenses(db, user_id)
    return incomes - expenses