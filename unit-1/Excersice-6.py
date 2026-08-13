#6) Write a program to illustrate the use of tuples and sets with basic operations.
colors = ("Red", "Green", "Blue")
print("Tuple:", colors)
print("First color:", colors[0])
print("Length of tuple:", len(colors))
# Set
fruits = {"Apple", "Banana", "Mango"}
print("Set:", fruits)
# Add an element
fruits.add("Orange")
print("After adding Orange:", fruits)
# Remove an element
fruits.remove("Banana")
print("After removing Banana:", fruits)
# Check if an element exists
print("Apple in set:", "Apple" in fruits)

#output
Tuple: ('Red', 'Green', 'Blue')
First color: Red
Length of tuple: 3
Set: {'Banana', 'Apple', 'Mango'}
After adding Orange: {'Banana', 'Apple', 'Mango', 'Orange'}
After removing Banana: {'Apple', 'Mango', 'Orange'}
Apple in set: True
