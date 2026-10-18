#8. Write a program to demonstrate encapsulation and abstraction using classes.

class Student:
    def __init__(self):
        self.__marks = 90

    def display(self):
        print("Marks:", self.__marks)

s1 = Student()
s1.display()

#output
Marks: 90

Objectives
To understand the concepts of encapsulation and abstraction in Python.
To learn how to protect data using private variables.
To understand the use of abstract classes and abstract methods.
To implement encapsulation and abstraction using classes in Python.
Conclusion

Thus, we successfully demonstrated encapsulation and abstraction using classes in Python. We learned how encapsulation protects data and abstraction hides implementation details using abstract methods.
