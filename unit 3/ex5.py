# Write a program to display current date and time using datetime module.

import datetime

now=datetime.datetime.now()

print("current date and time: ",now)

formatted_now = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date and Time:", formatted_now)

#output
current date and time:  2026-10-09 10:06:48.406227
Formatted Date and Time: 09-10-2026 10:06:48
