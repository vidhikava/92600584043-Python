#7. Write a program to demonstrate list dictionary and set comprehensions.
# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print("List comprehension:", squares)

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x * x for x in numbers}
print("Dictionary comprehension:", square_dict)

# Set comprehension
numbers = [1, 2, 2, 3, 3, 4, 5]
square_set = {x * x for x in numbers}
print("Set comprehension:", square_set)

#output
List comprehension: [1, 4, 9, 16, 25]
Dictionary comprehension: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Set comprehension: {1, 4, 9, 16, 25}

