#4)Write a program to demonstrate string operations including slicing formatting and built-in string functions.
print("\n---------string operations------\n")
text=" python programming"
print("original text:", text)
print("first 6 char: ",text[:7])
print("last 11 char: ",text[7:])
print("revered string: ",text[::-1])

print("\n---------built-in string functions------\n")
print("original text:", text)
print("Uppercase: ",text.upper())
print("Lower: ",text.lower())
print("capitalize: ",text.capitalize())
print("count: ",text.count("o"))
print("extra space: ",text.strip())
print("replace word: ",text.replace("programming","language"))

#output
--------string operations------

original text:  python programming
first 6 char:   python
last 11 char:   programming
revered string:  gnimmargorp nohtyp 

---------built-in string functions------

original text:  python programming
Uppercase:   PYTHON PROGRAMMING
Lower:   python programming
capitalize:   python programming
count:  2
extra space:  python programming
replace word:   python language





