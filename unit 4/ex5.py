#5. Write a program to implement single multilevel and multiple inheritance.
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def message(self):
        print("Class C")

class D:
    def hello(self):
        print("Class D")

class E(B, D):
    pass

obj = B()
obj.show()
obj.display()

obj2 = C()
obj2.show()
obj2.display()
obj2.message()

obj3 = E()
obj3.show()
obj3.hello()

#output
Class A
Class B
Class A
Class B
Class C
Class A
Class D

To understand the concept of inheritance in Python.
To learn how to implement single inheritance using a parent and child class.
To understand multilevel inheritance, where a class inherits from another derived class.
To learn how to implement multiple inheritance by inheriting from more than one parent class.

Thus, we successfully implemented single, multilevel, and multiple inheritance in Python. We learned how classes can inherit methods and properties from one or more parent classes.
