


candidate_file = open("Data.txt", "r")
# candidate_file = open("Data.txt", "w") write
# candidate_file = open("Data.txt", "a") append
# candidate_file = open("Data.txt", "r+") read+write

print(candidate_file.readable())

# print(candidate_file.readline())
# print(candidate_file.readline())
# print(candidate_file.readline())

# print(candidate_file.readlines()) (it is a array of lines)

for candidate in candidate_file.readlines():
    print(candidate)

candidate_file.close()

candidate_file1 = open("Data.txt", "a")
candidate_file1.write("Kartick - Chennai")
candidate_file1.close()

candidate_file2 = open("Data1.txt", "w")
candidate_file2.write("Kartick - Chennai")
candidate_file2.close()

