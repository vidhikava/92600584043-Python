#8. Write a program to illustrate variable scope using local global and nonlocal variables
x = 10
def outer():
    y = 20
    def inner():
        z = 30
        print("Local variable:", z)
        print("Nonlocal variable:", y)
        print("Global variable:", x)
    inner()
outer()

#output
Local variable: 30
Nonlocal variable: 20
Global variable: 10
