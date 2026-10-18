#3. Write a program to illustrate instance variables and class variables.
class Student:
    college = "Marwadi University"

    def __init__(self, name):
        self.name = name

s1 = Student("Vidhi")
s2 = Student("harita")

print("Student 1:", s1.name)
print("Student 2:", s2.name)
print("College:", Student.college)

#output
Student 1: Vidhi
Student 2: harita
College: Marwadi University

To understand the concept of instance variables and class variables in Python.
To learn how to declare instance variables inside the constructor.
To learn how to declare class variables inside a class.
To understand the difference between instance variables and class variables.

Thus, we successfully demonstrated instance variables and class variables in Python. We learned that instance variables store individual object data, while class variables are shared among all objects of a class.

