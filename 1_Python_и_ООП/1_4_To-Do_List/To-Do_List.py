import json

class Task:
    # описание задачи
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    # статус выполнения задачи (выполнена/не выполнена)
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
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

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w", encoding="utf-8") as file:
            tasks_data = [{"description": task.description, "completed": task.completed} for task in self.tasks]
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)
        print(f"Задачи сохранены в файл {filename}.")

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["description"], task["completed"]) for task in tasks_data]
            print(f"Задачи загружены из файла {filename}.")
        except FileNotFoundError:
            print("Файл с задачами не найден. Создан новый список задач.")

def main():
    todo_list = ToDoList()
    todo_list.load_from_file()

    while True:
        print("\nМеню:")
        print("1. Просмотреть задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Сохранить задачи")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            description = input("Введите описание задачи: ")
            todo_list.add_task(description)
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Введите номер задачи для отметки как выполненной: "))
            todo_list.mark_task_completed(task_number)
        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Введите номер задачи для удаления: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            todo_list.save_to_file()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()