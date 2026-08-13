#9) Write a program to define and use user-defined functions with different types of arguments.
def hello():
    print("Hello")
def greet(name):
    print("Hello", name)
def add(a, b):
    print("Sum =", a + b)
def city(name="Rajkot"):
    print("City:", name)

hello()
greet("Vidhi")
add(10, 20)
city()
city("Ahmedabad")

#output
Hello
Hello Vidhi
Sum = 30
City: Rajkot
City: Ahmedabad
