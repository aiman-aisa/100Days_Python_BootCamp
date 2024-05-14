# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:

# 1
# 2
# 3
# and file2.txt contained:

# 2
# 3
# 4
# result = [2, 3]

with open(r"Day-26-List-Comprehension\file1.txt") as file1:
    content1 = file1.readlines()
    content1 = [int(content.strip("\n")) for content in content1]
    print(content1)

with open(r"Day-26-List-Comprehension\file2.txt") as file1:
    content2 = file1.readlines()
    content2 = [int(content.strip("\n")) for content in content2]
    print(content2)
    
result = [num1 for num1 in content1 if num1 in content2]
print(result)