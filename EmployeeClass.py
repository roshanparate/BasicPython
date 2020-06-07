class Employee:

    def __init__(self, name , id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def is_salary_greater_than_lack(self):
        SAL_CONTANT = 100000.00
        if self.salary > SAL_CONTANT:
            return True
        else:
            return False
