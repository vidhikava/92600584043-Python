#9. Write a program to demonstrate iterators and iterables in Python.
numbers = [10, 20, 30, 40, 50]
print("Iterable:")
for num in numbers:
    print(num)

print("\nIterator:")
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#output
Iterable:
10
20
30
40
50

Iterator:
10
20
30
40
50
