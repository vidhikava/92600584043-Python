#8. Write a program to demonstrate basic regular expression pattern matching.

import re

text = "The quick brown fox jumps over 2 lazy dogs."

if re.search(r"fox", text):
    print("Found the word 'fox' in the text.")

numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

masked_text = re.sub(r"[aeiouAEIOU]", "*", text)
print("Text with vowels masked:", masked_text)

#output
Found the word 'fox' in the text.
Numbers found: ['2']
Text with vowels masked: Th* q**ck br*wn f*x j*mps *v*r 2 l*zy d*gs.
