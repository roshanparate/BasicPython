"""
This file have some example of
* conditions: if, elif and else in python
* operator: or & and in python
* not() function
* compairator: <, >, ==, <=, >=, !=
"""

""" ************************************************************** """
is_happy = False
is_sad = True

if is_happy or is_sad:
    print("you are happy")
else:
    print("you are sad")

""" ************************************************************** """
is_happy = True
is_sad = False

if is_happy and is_sad:
    print("you are happy")
elif not(is_sad):
    print("you are not happy but sad")
else:
    print("you are sad")

""" ************************************************************** """
is_happy = False
is_sad = True

if is_happy and is_sad:
    print("you are happy")
elif not(is_sad):
    print("you are not happy but sad")
else:
    print("you are sad")

""" ************************************************************** """


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(23, 4, 5))