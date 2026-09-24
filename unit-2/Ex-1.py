# 1. Write a program to demonstrate conditional statements using if if-else and if-elif-else.

#  if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")

#if-else statement
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# if-elif-else statement
marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

#output
Enter your age: 20
You are eligible to vote.
Enter a number: 5
Number is odd.
Enter your marks: 99
Grade: A
