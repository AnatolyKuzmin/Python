# finance_tracker/cli.py
from .database import get_db
from . import crud

def display_menu():
    print("1. Просмотреть все операции")
    print("2. Добавить операцию")
    print("3. Редактировать операцию")
    print("4. Удалить операцию")
    print("5. Фильтровать операции")
    print("6. Выйти")

def main():
    db = next(get_db())

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            transactions = crud.get_user_transactions(db, user_id=1)
            for transaction in transactions:
                print(transaction)
        elif choice == "2":
            amount = float(input("Введите сумму: "))
            transaction_type = input("Введите тип (income/expense): ")
            category_id = int(input("Введите ID категории: "))
            crud.add_transaction(db, user_id=1, category_id=category_id, amount=amount, transaction_type=transaction_type)
            print("Операция добавлена.")
        elif choice == "3":
            transaction_id = int(input("Введите ID операции: "))
            amount = float(input("Введите новую сумму: "))
            transaction_type = input("Введите новый тип (income/expense): ")
            category_id = int(input("Введите новый ID категории: "))
            updated_transaction = crud.update_transaction(db, transaction_id=transaction_id, amount=amount, type=transaction_type, category_id=category_id)
            if updated_transaction:
                print("Операция обновлена.")
            else:
                print("Операция не найдена.")
        elif choice == "4":
            transaction_id = int(input("Введите ID операции: "))
            if crud.delete_transaction(db, transaction_id=transaction_id):
                print("Операция удалена.")
            else:
                print("Операция не найдена.")
        elif choice == "5":
            filter_type = input("Фильтровать по типу (income/expense): ")
            transactions = crud.get_transactions_by_type(db, user_id=1, transaction_type=filter_type)
            for transaction in transactions:
                print(transaction)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()