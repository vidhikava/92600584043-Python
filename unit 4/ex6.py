#6. Write a program to demonstrate method overriding and polymorphism.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a1 = Dog()
a2 = Cat()

a1.sound()
a2.sound()

#output
Dog barks
Cat meows

To understand the concepts of method overriding and polymorphism in Python.
To learn how a child class can redefine a method of its parent class.
To demonstrate polymorphism by calling the same method on different objects.
To understand how the same method can perform different actions depending on the object.

Thus, we successfully demonstrated method overriding and polymorphism in Python. We learned how different classes can use the same method name to perform different actions.
