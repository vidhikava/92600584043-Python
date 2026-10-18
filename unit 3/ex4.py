#Write a program to generate random numbers using random module.

import random

random_int=random.randint(1,100)
print (f"random integer(1-100): {random_int}")

random_float = random.random()
print(f"Random Float (0.0-1.0): {random_float}")

options = ["apple", "banana", "cherry", "date"]
random_item = random.choice(options)
print(f"Random Item: {random_item}")

#output
random integer(1-100): 13
Random Float (0.0-1.0): 0.5009710255943646
Random Item: date

