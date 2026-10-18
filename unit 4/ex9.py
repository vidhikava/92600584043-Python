#9. Write a program to read and write data into a file using different file modes.
f = open("data.txt", "w")
f.write("Hello Python")
f.close()

f = open("data.txt", "r")
print(f.read())
f.close()

f = open("data.txt", "a")
f.write("\nWelcome to Python")
f.close()

f = open("data.txt", "r")
print(f.read())
f.close()

#output
Hello Python
Hello Python
Welcome to Python

To understand file handling in Python.
To learn how to open and close files using the open() and close() functions.
To perform read, write, and append operations using different file modes.
To understand the use of r, w, and a file modes.

Thus, we successfully performed read, write, and append operations on a file using Python. We learned how to use different file modes to store and retrieve data from a file.
