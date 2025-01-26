from abc import ABC, abstractmethod

# абстрактный класс SalaryCalculator,
# который будет определять метод calculate_salary.
class SalaryCalculator(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
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

# Миксин EmailNotifier добавляет функциональность отправки
# уведомлений по электронной почте при изменении зарплаты сотрудника
class EmailNotifier:
    def send_email(self, message):
        print(f"Отправка email: {message}")

    def notify_salary_change(self, old_salary, new_salary):
        message = f"Зарплата изменена с {old_salary} на {new_salary}"
        self.send_email(message)

# Класс Designer наследует от Employee
# и добавляет атрибуты fixed_salary (фиксированная зарплата)
# и bonus (бонус)
class Designer(Employee, EmailNotifier):
    def __init__(self, name, employee_id, fixed_salary, bonus):
        super().__init__(name, employee_id)
        self.fixed_salary = fixed_salary
        self.bonus = bonus
        self._salary = self.calculate_salary()

    def calculate_salary(self):
        return self.fixed_salary + self.bonus

    def set_salary(self, fixed_salary, bonus):
        old_salary = self._salary
        self.fixed_salary = fixed_salary
        self.bonus = bonus
        self._salary = self.calculate_salary()
        self.notify_salary_change(old_salary, self._salary)

    def display_info(self):
        return f"{super().display_info()}, Должность: Дизайнер, Зарплата: {self.calculate_salary()}"
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

# класс EmployeeReport, который будет реализовывать
# метод generate_report для создания отчетов о сотрудниках.
class EmployeeReport(ReportGenerator):
    def __init__(self, employees):
        self.employees = employees

    def generate_report(self):
        report = "Отчет о сотрудниках:\n"
        for employee in self.employees:
            report += employee.display_info() + "\n"
        return report

# Пример использования
# Создание объектов
manager = Manager("Иван Иванов", 1, 50000, 10000)
developer = Developer("Петр Петров", 2, 2000, 160)
intern = Intern("Алексей Алексеев", 3, 10000)
designer = Designer("Мария Иванова", 4, 40000, 5000)

# Вывод информации о сотрудниках
employees = [manager, developer, intern]
for employee in employees:
    print(employee.display_info())

print()
print(manager.display_info())

# Изменение зарплаты дизайнера
designer.set_salary(45000, 6000)

# Создание отчета
employees = [manager, developer, intern, designer]
report = EmployeeReport(employees)
print(report.generate_report())