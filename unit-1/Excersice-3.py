#3)Write a program to perform arithmetic relational and logical operations using Pythonoperators.
a=int(input("enter number1: "))
b=int(input("enter number2: "))

print("\n----------------Arithmetic operations.-------------------\n")
print("add: ",a+b)
print("sub: ",a-b)
print("mul: ",a*b)
print("div: ",a/b)
print("mod: ", a%b)

print("\n----------------relational operations.-------------------\n")
print("a is : ",a,"::","b is:",b,"::",a==b)
print("a is : ",a,"::","b is:",b,"::",a!=b)
print("a is : ",a,"::","b is:",b,"::",a>=b)
print("a is : ",a,"::","b is:",b,"::",a<=b)
print("a is : ",a,"::","b is:",b,"::",a>b)
print("a is : ",a,"::","b is:",b,"::",a<b)

print("\n----------------logical operations.-------------------\n")
print("a is : ",a,"::","b is:",b,"::",a==b and a>=b)
print("a is : ",a,"::","b is:",b,"::",a>b and a<=b)
print("a is : ",a,"::","b is:",b,"::",a>=b)

#output
enter number1: 34
enter number2: 34

----------------Arithmetic operations.-------------------

add:  68
sub:  0
mul:  1156
div:  1.0
mod:  0

----------------relational operations.-------------------

a is :  34 :: b is: 34 :: True
a is :  34 :: b is: 34 :: False
a is :  34 :: b is: 34 :: True
a is :  34 :: b is: 34 :: True
a is :  34 :: b is: 34 :: False
a is :  34 :: b is: 34 :: False

----------------logical operations.-------------------

a is :  34 :: b is: 34 :: True
a is :  34 :: b is: 34 :: False
a is :  34 :: b is: 34 :: True
