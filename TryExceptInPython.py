

'''
input: abc
number = int(input("Enter number : "))
print(number)
'''

'''
try:
    number = int(input("Enter number : "))
    print(number)
except:
    print("invalid input")
'''

try:
    # num = 10/0
    number = int(input("Enter number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print("Invalid Value..")