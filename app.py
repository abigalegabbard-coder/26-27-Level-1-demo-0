print("Hello, World")

# Hashtags in Pyton cannot be used for line comments
# this will not be run or interperted by python

#Our first variable!
first_name = "Bill" #Note: this is a string. It is surrounded by quotes ""
print(first_name)
sport = "Cross Country"

#fstrings - allow you to embed variables into strings
print(f"{first_name} likes {sport}")

#int (or interger) demo:
age = 100
# "Bill likes Cross Country and is 100 years old"
print(f"{first_name} likes {sport} and is {age} years old")

# floats (decimal numbers)
gpa = 1.89
print(f"Unfortunately, (first_name)'s gpa is {gpa}")

#booleans (true/false)
allowed_to_play = True
print(f"{first_name} is allowed to play:{allowed_to_play}")

#demo of an if statement!
if allowed_to_play:
    print(f"{first_name} is allowed to play! Huzzah!")
else:
    print(f"{first_name} cannot play. What a bum.")

triangle = False
if triangle:
    print("     .  ")
    print("    . . ")
    print("   .   . ")
    print("  .     . ")
    print(" ......... ")
else:
    print(" _____")
    print("|     |")
    print("|     |")
    print("|_____|")

