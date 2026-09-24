#5. Write a program to demonstrate the use of break continue and pass statements.
# break statement
print("Using break:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# continue statement
print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass statement
print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

#output
Using break:
1
2
3
Using continue:
1
2
4
5
Using pass:
1
2
3
4
5


