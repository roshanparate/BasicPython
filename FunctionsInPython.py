"""
This file have some example of Function and return in python
"""


def first_fun_to_say_hi(name, age, code ):
    print("hello "+ name +", Your age is " + age + " and your code is " + str(code))


first_fun_to_say_hi("Mike", "23", 123)


def cube(num):
    return num * num * num


result = cube(3)
print(result)