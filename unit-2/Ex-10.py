#10.Write a program to generate a sequence of numbers using generator functions and yield keyword.
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter the number: "))

print("Sequence of numbers:")

for num in generate_numbers(n):
    print(num)

#output
Enter the number: 5
Sequence of numbers:
1
2
3
4
5
