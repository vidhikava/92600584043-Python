#7. Write a program to illustrate method resolution order and magic methods.
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    pass

obj = C()
obj.show()

print(C.mro())

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s1 = Student("Vidhi")
print(s1)
#output
Class B
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
Vidhi

To understand the concept of Method Resolution Order (MRO) in Python.
To learn how Python determines the order in which methods are searched in inheritance.
To understand magic methods such as __init__() and __str__().
To demonstrate how magic methods work automatically in Python classes.

Thus, we successfully demonstrated Method Resolution Order (MRO) and magic methods in Python. We learned how Python searches for methods in an inheritance hierarchy and how magic methods define the behavior of objects.
