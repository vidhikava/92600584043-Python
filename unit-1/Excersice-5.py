#5) Write a program to create and manipulate lists using indexing slicing and list comprehensions.
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
# Indexing
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
# Slicing
print("First three fruits:", fruits[:3])
print("Last two fruits:", fruits[3:])
# Manipulating the list
fruits.append("Pineapple")
print("After adding Pineapple:", fruits)
fruits.remove("Mango")
print("After removing Mango:", fruits)
# List comprehension
upper_fruits = [fruit.upper() for fruit in fruits]
print("Fruits in uppercase:", upper_fruits)

#output
First fruit: Apple
Last fruit: Grapes
First three fruits: ['Apple', 'Banana', 'Mango']
Last two fruits: ['Orange', 'Grapes']
After adding Pineapple: ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Pineapple']
After removing Mango: ['Apple', 'Banana', 'Orange', 'Grapes', 'Pineapple']
Fruits in uppercase: ['APPLE', 'BANANA', 'ORANGE', 'GRAPES', 'PINEAPPLE']
