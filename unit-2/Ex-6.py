#6. Write a program to iterate over lists strings and dictionaries using loops.
# Iterate over a list
print("List:")
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
print("\nString:")
name = "Python"
for char in name:
    print(char)

# Iterate over a dictionary
print("\nDictionary:")
student = {
    "Name": "Vidhi",
    "Age": 20,
    "Course": "MCA"
}
for key, value in student.items():
    print(key, ":", value)

#output
List:
Apple
Banana
Mango

String:
P
y
t
h
o
n

Dictionary:
Name : Vidhi
Age : 20
Course : MCA

