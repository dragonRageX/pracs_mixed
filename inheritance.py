class Employee():
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def introduce(self):
        print(f"Employee {self.emp_id}: {self.name}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_lang):
        super().__init__(name, emp_id)
        self.programming_lang = programming_lang

    def introduce(self):
        print(f"Developer {self.emp_id}: {self.name} (Language: {self.programming_lang})")

class Tester(Employee):
    def __init__(self, name, emp_id, testing_type):
        super().__init__(name, emp_id)
        self.testing_type = testing_type

    def introduce(self):
        print(f"Tester {self.emp_id}: {self.name} (Testing Type: {self.testing_type})")

class Manager(Employee):
    def __init__(self, name, emp_id):
        super().__init__(name, emp_id)
        self.managed_employees = []

    def introduce(self):
        print(f"Manager {self.emp_id}: {self.name}")

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def remove_employee(self, employee):
        self.managed_employees.remove(employee)

    def display_managed_employees(self):
        for employee in self.managed_employees:
            employee.introduce()
        print()

dev1 = Developer("Param", 1, "Python")
tester1 = Tester("Gaurav", 2, "Manual Testing")
manager1 = Manager("Siddh", 3)

manager1.add_employee(dev1)
manager1.add_employee(tester1)

manager1.display_managed_employees()

print("Hi")

manager1.remove_employee(dev1)

manager1.display_managed_employees()