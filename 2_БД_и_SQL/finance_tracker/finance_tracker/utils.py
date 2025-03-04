# finance_tracker/utils.py
from sqlalchemy.orm import Session
from . import models
import csv

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

def export_transactions_to_csv(db: Session, user_id: int, filename: str = "transactions.csv"):
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()

    if not transactions:
        print("Нет операций для экспорта.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Сумма", "Тип", "Категория", "Дата"])

        for transaction in transactions:
            writer.writerow([
                transaction.id,
                transaction.amount,
                transaction.type,
                transaction.category.name,
                transaction.date
            ])

    print(f"Операции экспортированы в файл {filename}.")