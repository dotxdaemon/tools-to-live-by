#!/usr/bin/python
age = float(input("What is your current age?\n"))
death = int(input("At what age do you think you will die?\n"))

days = round((death - age) * 365)
weeks = round((death - age) * 52)
month = round((death - age) * 12)

print(f"You have {days} days, {weeks} weeks and {month} months left to live. What will you do?")
