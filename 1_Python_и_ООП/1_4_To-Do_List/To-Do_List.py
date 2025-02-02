import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
    
class ToDoList:
    def __init__(self, name):
        self.name = name
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

    def edit_task(self, task_number, new_description):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].description = new_description
            print(f"Задача {task_number} отредактирована.")
        else:
            print("Неверный номер задачи.")

    def sort_tasks(self, completed_first=True):
        self.tasks.sort(key=lambda task: task.completed == completed_first, reverse=True)
        print("Задачи отсортированы.")

    def save_to_file(self, filename=None):
        if not filename:
            filename = f"{self.name}.json"
        with open(filename, "w", encoding="utf-8") as file:
            tasks_data = [{"description": task.description, "completed": task.completed} for task in self.tasks]
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)
        print(f"Задачи сохранены в файл {filename}.")

    def load_from_file(self, filename=None):
        if not filename:
            filename = f"{self.name}.json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["description"], task["completed"]) for task in tasks_data]
            print(f"Задачи загружены из файла {filename}.")
        except FileNotFoundError:
            print("Файл с задачами не найден. Создан новый список задач.")

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
        print("8. Сортировать задачи")
        print("9. Сохранить задачи")
        print("10. Выйти")

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
                current_list.add_task(description)
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
                sort_order = input("Сортировать по выполненным задачам сначала? (да/нет): ").lower()
                current_list.sort_tasks(sort_order == "да")
            else:
                print("Список задач не выбран.")
        elif choice == "9":
            if current_list:
                current_list.save_to_file()
            else:
                print("Список задач не выбран.")
        elif choice == "10":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()