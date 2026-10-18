#10.Write a program to perform file pointer operations using seek and tell methods.
f = open("data.txt", "w")
f.write("Hello Python")
f.close()

f = open("data.txt", "r")

print("Position:", f.tell())

f.seek(6)
print("Position after seek:", f.tell())

print("Data:", f.read())

f.close()
#output
Position: 0
Position after seek: 6
Data: Python

To understand file pointer operations in Python.
To learn how to use the tell() method to find the current file pointer position.
To learn how to use the seek() method to move the file pointer to a specific position.
To perform file reading operations using file pointer methods.
Conclusion

Thus, we successfully demonstrated file pointer operations using the seek() and tell() methods in Python. We learned how to find and change the file pointer position while reading a file.
