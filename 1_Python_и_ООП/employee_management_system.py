from abc import ABC, abstractmethod

# абстрактный класс SalaryCalculator,
# который будет определять метод calculate_salary.
class SalaryCalculator(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

# базовый класс Employee,
# который будет содержать общие атрибуты
# и методы для всех сотрудников
class Employee(SalaryCalculator):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"ID: {self.employee_id}, Имя: {self.name}"
    
    def calculate_salary(self):
        raise NotImplementedError("Метод calculate_salary должен быть реализован в дочернем классе")

# Создадим миксин Loggable,
# который будет добавлять функциональность логирования.
class Loggable:
    def log(self, message):
        print(f"Лог: {message}")

# класс Manager наследует от Employee
# и добавляет атрибут bonus (бонус),
# а также реализует метод calculate_salary
class Manager(Employee, Loggable):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        self.log(f"Расчет зарплаты для менеджера {self.name}")
        return self.salary + self.bonus
    
    def display_info(self):
        return f"{super().display_info()}, Должность: Менеджер, Зарплата: {self.calculate_salary()}"
    
# класс Developer наследует от Employee
# и добавляет атрибут hourly_rate (почасовая ставка)
# и hours_worked (отработанные часы),
# а также реализует метод calculate_salary.
class Developer(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        return f"{super().display_info()}, Должность: Разработчик, Зарплата: {self.calculate_salary()}"

# класс Intern наследует от Employee
# и добавляет атрибут stipend (стипендия),
# а также реализует метод calculate_salary.
class Intern(Employee):
    def __init__(self, name, employee_id, stipend):
        super().__init__(name, employee_id)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    
    def display_info(self):
        return f"{super().display_info()}, Должность: Стажер, Зарплата: {self.calculate_salary()}"


# Пример использования
# Создание объектов
manager = Manager("Иван Иванов", 1, 50000, 10000)
developer = Developer("Петр Петров", 2, 2000, 160)
intern = Intern("Алексей Алексеев", 3, 10000)

# Вывод информации о сотрудниках
employees = [manager, developer, intern]
for employee in employees:
    print(employee.display_info())

print()
print(manager.display_info())
