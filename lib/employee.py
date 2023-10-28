class Employee:
    all = []

    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        type(self).all.append(self)

    def manager_name(self):
        return self.manager.name

    def tax_bracket(self):
        pass

    @classmethod
    def paid_over(cls, amt):
        return [emp for emp in cls.all if emp.salary > amt]

    @classmethod
    def find_by_department(cls, dep):
        return next((emp for emp in cls.all if emp.manager.department == dep))
