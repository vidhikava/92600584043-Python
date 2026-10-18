#7. Write a program to copy move and delete files using shutil module.

import os
import shutil

open("a.txt", "w").close()
os.mkdir("my_folder")

shutil.copy("a.txt", "b.txt")
print("1. File copied!")

shutil.move("b.txt", "c.txt")
print("2. File moved!")

shutil.rmtree("my_folder")
print("3. Folder deleted!")

#output
1. File copied!
2. File moved!
3. Folder deleted!
