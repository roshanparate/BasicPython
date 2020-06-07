

cities = ["Mumbai", "Pune", "Delhi", "Hyderabad"]

print(cities)
cities[3] = "Nagpur"

print(cities)
print(cities[1])
print(cities[-1])
print(cities[2:])

code = [34, 2, 5, 6, 76, 56, 34, 22]

""" add list in another list """
cities.extend(code)
print(cities)
cities.clear()

cities_new = ["Mumbai", "Pune", "Delhi", "Hyderabad"]

""" insert in list """
cities_new.insert(2, "Bhopl")
print(cities_new)

""" append list  """
cities_new.append("Jaipur")
print(cities_new)

""" sort the list """
cities_new.sort()
print(cities_new)

code.sort()
print(code)

""" copy the list """
code_copy = code.copy()
print(code_copy)

code_copy = [234, 123, 432, 567, 765, 876, 123]

""" pop  and remove from the list"""
code_copy.pop()
print(code_copy)

code_copy.remove(567)
print(code_copy)

code_copy.reverse()
print(code_copy)
print(code_copy.count(123))
print(code.index(34))

print("\n")

""" 2D List """
number =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number[0][0])

