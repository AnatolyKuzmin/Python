# finance_tracker/main.py
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models

def main():
    db = next(get_db())

    # Пример использования CRUD-функций
    user = crud.create_user(db, name="Alice", email="alice@example.com")
    print(f"Создан пользователь: {user.name}")

    transaction = crud.add_transaction(db, user_id=user.id, category_id=1, amount=1000, transaction_type="income")
    print(f"Добавлена операция: {transaction.amount}")

if __name__ == "__main__":
    main()