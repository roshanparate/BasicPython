


""" while loop start """
i = 1

while i<=5:
    print(i)
    i += 1

print("\n")
""" while loop end """

""" for loop start """

for letter in "Welcome to python program":
    print(letter)

print("\n")

city_name = ["Jaipur", "Pune", "munbai", "Delhi"]
for name in city_name:
    print(name)

print("\n")

for index in range(len(city_name)):
    print(city_name[index])

""" for loop End """

print("\n")

number =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for grid in number:
    for value in grid:
        print(value)