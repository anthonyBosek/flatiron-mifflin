class Manager:
    all = []

    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        self.employees = []
        type(self).all.append(self)

    def hire_employee(self, name, salary):
        self.employees.append((name, salary))

    @classmethod
    def all_departments(cls):
        return [mngr.department for mngr in cls.all]

    @classmethod
    def average_age(cls):
        ages = [mngr.age for mngr in cls.all]
        return sum(ages) / len(ages)
