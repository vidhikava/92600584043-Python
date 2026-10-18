#4. Write a program to demonstrate instance methods class methods and static methods.
class Student:
    college = "Marwadi University"

    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls):
        print("College:", cls.college)

    @staticmethod
    def static_method():
        print("This is a static method.")

s1 = Student()

s1.instance_method()
Student.class_method()
Student.static_method()

#output
This is an instance method.
College: Marwadi University
This is a static method.

To understand instance methods, class methods, and static methods in Python.
To learn how to define an instance method using self.
To learn how to define a class method using @classmethod and cls.
To learn how to define a static method using @staticmethod.

Thus, we successfully demonstrated instance methods, class methods, and static methods in Python. We learned how each method is defined and called within a class.
