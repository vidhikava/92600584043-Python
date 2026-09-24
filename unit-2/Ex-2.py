#2. Write a program to check whether a number is positive negative or zero using nested conditions.
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

#output
Enter a number: 3
The number is positive.
