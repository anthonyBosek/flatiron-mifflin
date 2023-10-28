class Manager:
    all = []

    __slots__ = ["_name", "_department", "_age", "_employees"]

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.employees = []
        self.save()

    def save(self):
        type(self).all.append(self)

    @classmethod
    def all_departments(cls):
        return [mngr.department for mngr in cls.all]

    @classmethod
    def average_age(cls):
        ages = [mngr.age for mngr in cls.all]
        return float(sum(ages) / len(ages), 2)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type String.")
        else:
            self._name = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if not isinstance(value, str):
            raise TypeError("Department must be of type String.")
        else:
            self._department = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be of type Integer.")
        else:
            self._age = value

    # @property
    # def employees(self):
    #     return self._employees

    # @employees.setter
    # def employees(self, value):
    #     name, salary = value
    #     if not isinstance(name, str):
    #         raise TypeError("Employee name must of type String")
    #     elif not isinstance(salary, float):
    #         raise TypeError("Employee salary must be of type Float")
    #     elif hasattr(self, "employee"):
    #         self._employees.append((name, salary))
    #     else:
    #         self._employees = [(name, salary)]

    # def hire_employee(self, name, salary):
    #     self.employees.append()
