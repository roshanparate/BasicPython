import FunctionsInPython
from EmployeeClass import Employee

print(FunctionsInPython.cube(2))

employee = Employee("John", 1 , 100000.00)
employee1 = Employee("Alok", 2 , 200000.00)
print(employee.name)
print(employee.salary)

print(employee1.salary)

print(employee.is_salary_greater_than_lack())
print(employee1.is_salary_greater_than_lack())