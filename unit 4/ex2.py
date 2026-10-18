#2. Write a program to demonstrate constructor and destructor usage.
class Student:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

s1 = Student()
del s1

#output
Constructor called
Destructor called

To understand the concept of constructors and destructors in Python.
To learn how to define a constructor using __init__().
To learn how to define a destructor using __del__().

Thus, we successfully demonstrated the use of constructors and destructors in Python. We learned how constructors initialize objects and destructors perform cleanup when objects are destroyed
To understand how constructors and destructors work during object creation and destruction.
