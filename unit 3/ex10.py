#10.Write a program to extract specific information from a text file using regular expressions.import re

import re
with open("info.txt", "w") as file:
    file.write("Call me at 123-456-7890 or 987-654-3210.")

with open("info.txt", "r") as file:
    text = file.read()

numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)

print("Extracted Numbers:", numbers)

#output
Extracted Numbers: ['123-456-7890', '987-654-3210']
