#6. Write a program to perform file and directory operations using os and sys modules.

import os
import sys

print("OS Platform:", sys.platform)

print("Current Directory:", os.getcwd())

os.mkdir("my_folder")
print("Folder created successfully!")

os.rmdir("my_folder")
print("Folder deleted successfully!")

#output
OS Platform: win32
Current Directory: D:\MCA\Pyhton\unit 3
Folder created successfully!
Folder deleted successfully!
