#9. Write a program to use re module functions such as match search and findall.
import re

text = "apple banana apple"

m = re.match(r"apple", text)
print("1. match():", m.group())

s = re.search(r"banana", text)
print("2. search():", s.group())

f = re.findall(r"apple", text)
print("3. findall():", f)

#output
1. match(): apple
2. search(): banana
3. findall(): ['apple', 'apple']
