import json
import csv
from datetime import datetime

class Task:
    def __init__(self, description, completed=False, deadline=None, priority="средний", category=None):
        self.description = description
        self.completed = completed
        self.deadline = deadline
        self.priority = priority
        self.category = category

    def __str__(self):
        status = "✓" if self.completed else "✗"
        deadline_info = f", Дедлайн: {self.deadline}" if self.deadline else ""
        priority_info = f", Приоритет: {self.priority}" if self.priority else ""
        category_info = f", Категория: {self.category}" if self.category else ""
        return f"[{status}] {self.description}{deadline_info}{priority_info}{category_info}"
    
class ToDoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, description, deadline=None, priority="средний", category=None):
        task = Task(description, deadline=deadline, priority=priority, category=category)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print(f"Задача {task_number} отмечена как выполненная.")
        else:
            print("Неверный номер задачи.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Задача '{deleted_task.description}' удалена.")
        else:
            print("Неверный номер задачи.")

    def edit_task(self, task_number, new_description):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].description = new_description
            print(f"Задача {task_number} отредактирована.")
        else:
            print("Неверный номер задачи.")

    def set_deadline(self, task_number, deadline):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].deadline = deadline
            print(f"Для задачи {task_number} установлен дедлайн: {deadline}.")
        else:
            print("Неверный номер задачи.")

    def set_priority(self, task_number, priority):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].priority = priority
            print(f"Для задачи {task_number} установлен приоритет: {priority}.")
        else:
            print("Неверный номер задачи.")

    def set_category(self, task_number, category):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].category = category
            print(f"Для задачи {task_number} установлена категория: {category}.")
        else:
            print("Неверный номер задачи.")

    def sort_tasks(self, completed_first=True):
        self.tasks.sort(key=lambda task: task.completed == completed_first, reverse=True)
        print("Задачи отсортированы.")

    def save_to_file(self, filename=None):
        if not filename:
            filename = f"{self.name}.json"
        with open(filename, "w", encoding="utf-8") as file:
            tasks_data = [{"description": task.description, "completed": task.completed, "deadline": task.deadline, "priority": task.priority, "category": task.category} for task in self.tasks]
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)
        print(f"Задачи сохранены в файл {filename}.")

    def load_from_file(self, filename=None):
        if not filename:
            filename = f"{self.name}.json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["description"], task["completed"], task["deadline"], task["priority"], task["category"]) for task in tasks_data]
            print(f"Задачи загружены из файла {filename}.")
        except FileNotFoundError:
            print("Файл с задачами не найден. Создан новый список задач.")

    def export_to_csv(self, filename=None):
        if not filename:
            filename = f"{self.name}.csv"
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Описание", "Статус", "Дедлайн", "Приоритет", "Категория"])
            for task in self.tasks:
                status = "Выполнена" if task.completed else "Не выполнена"
                writer.writerow([task.description, status, task.deadline, task.priority, task.category])
        print(f"Задачи экспортированы в файл {filename}.")

    def check_deadlines(self):
        today = datetime.today().date()
        for task in self.tasks:
            if task.deadline:
                deadline_date = datetime.strptime(task.deadline, "%Y-%m-%d").date()
                if deadline_date == today:
                    print(f"Напоминание: задача '{task.description}' должна быть выполнена сегодня.")
                elif deadline_date < today:
                    print(f"Напоминание: задача '{task.description}' просрочена.")

def main():
    lists = {}
    current_list = None

    while True:
        print("\nМеню:")
        print("1. Создать новый список задач")
        print("2. Выбрать список задач")
        print("3. Просмотреть задачи")
        print("4. Добавить задачу")
        print("5. Отметить задачу как выполненную")
        print("6. Удалить задачу")
        print("7. Редактировать задачу")
        print("8. Установить дедлайн для задачи")
        print("9. Установить приоритет для задачи")
        print("10. Установить категорию для задачи")
        print("11. Сортировать задачи")
        print("12. Сохранить задачи")
        print("13. Экспортировать задачи в CSV")
        print("14. Удалить список задач")
        print("15. Проверить дедлайны")
        print("16. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            list_name = input("Введите название списка задач: ")
            lists[list_name] = ToDoList(list_name)
            current_list = lists[list_name]
            print(f"Список задач '{list_name}' создан.")
        elif choice == "2":
            list_name = input("Введите название списка задач: ")
            if list_name in lists:
                current_list = lists[list_name]
                print(f"Выбран список задач '{list_name}'.")
            else:
                print("Список задач не найден.")
        elif choice == "3":
            if current_list:
                current_list.view_tasks()
            else:
                print("Список задач не выбран.")
        elif choice == "4":
            if current_list:
                description = input("Введите описание задачи: ")
                deadline = input("Введите дедлайн (опционально, формат ГГГГ-ММ-ДД): ")
                priority = input("Введите приоритет (высокий, средний, низкий): ")
                category = input("Введите категорию (опционально): ")
                current_list.add_task(description, deadline if deadline else None, priority, category if category else None)
            else:
                print("Список задач не выбран.")
        elif choice == "5":
            if current_list:
                current_list.view_tasks()
                task_number = int(input("Введите номер задачи для отметки как выполненной: "))
                current_list.mark_task_completed(task_number)
            else:
                print("Список задач не выбран.")
        elif choice == "6":
            if current_list:
                current_list.view_tasks()
                task_number = int(input("Введите номер задачи для удаления: "))
                current_list.delete_task(task_number)
            else:
                print("Список задач не выбран.")
        elif choice == "7":
            if current_list:
                current_list.view_tasks()
                task_number = int(input("Введите номер задачи для редактирования: "))
                new_description = input("Введите новое описание задачи: ")
                current_list.edit_task(task_number, new_description)
            else:
                print("Список задач не выбран.")
        elif choice == "8":
            if current_list:
                current_list.view_tasks()
                task_number = int(input("Введите номер задачи для установки дедлайна: "))
                deadline = input("Введите дедлайн (формат ГГГГ-ММ-ДД): ")
                current_list.set_deadline(task_number, deadline)
            else:
                print("Список задач не выбран.")
        elif choice == "9":
            if current_list:
                current_list.view_tasks()
                task_number = int(input("Введите номер задачи для установки приоритета: "))
                priority = input("Введите приоритет (высокий, средний, низкий): ")
                current_list.set_priority(task_number, priority)
            else:
                print("Список задач не выбран.")
        elif choice == "10":
            if current_list:
                current_list.view_tasks()
                task_number = int(input("Введите номер задачи для установки категории: "))
                category = input("Введите категорию: ")
                current_list.set_category(task_number, category)
            else:
                print("Список задач не выбран.")
        elif choice == "11":
            if current_list:
                sort_order = input("Сортировать по выполненным задачам сначала? (да/нет): ").lower()
                current_list.sort_tasks(sort_order == "да")
            else:
                print("Список задач не выбран.")
        elif choice == "12":
            if current_list:
                current_list.save_to_file()
            else:
                print("Список задач не выбран.")
        elif choice == "13":
            if current_list:
                current_list.export_to_csv()
            else:
                print("Список задач не выбран.")
        elif choice == "14":
            list_name = input("Введите название списка задач для удаления: ")
            if list_name in lists:
                del lists[list_name]
                print(f"Список задач '{list_name}' удален.")
            else:
                print("Список задач не найден.")
        elif choice == "15":
            if current_list:
                current_list.check_deadlines()
            else:
                print("Список задач не выбран.")
        elif choice == "16":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()