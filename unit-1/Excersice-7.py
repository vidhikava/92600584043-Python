#7) Write a program to create a dictionary and demonstrate dictionary methods and iteration.
student = {
    "Name": "Vidhi",
    "Age": 21,
    "City": "Rajkot"
}
print("Dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
student["Course"] = "MCA"
print("After adding Course:", student)
print("Dictionary items:")
for key, value in student.items():
    print(key, ":", value)

#output
Dictionary: {'Name': 'Vidhi', 'Age': 21, 'City': 'Rajkot'}
Keys: dict_keys(['Name', 'Age', 'City'])
Values: dict_values(['Vidhi', 21, 'Rajkot'])
After adding Course: {'Name': 'Vidhi', 'Age': 21, 'City': 'Rajkot', 'Course': 'MCA'}
Dictionary items:
Name : Vidhi
Age : 21
City : Rajkot
Course : MCA
    
