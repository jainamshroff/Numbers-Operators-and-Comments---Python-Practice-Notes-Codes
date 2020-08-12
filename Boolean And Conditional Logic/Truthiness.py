# Truthiness and Falsiness

"""
The conditional logic always boils down to True or False and using that
the condition is opted in or opted out
"""

x = 1

# print(x == 1)
# print(x != 1)

"""
Naturally False: empty objects, empty strings, None and zero
They are false on their own, but it doesn't means just by referencing zero it does not means its false

"""

if 0:
    print("This will be printed only if 0 is true")


if 1:
    print("Number 1 is inherently Truthy")

animal = input("Enter Your Fav Animal: ")

# if animal is empty this will not print
if animal:
    print(f"{animal} is my fav too!")
else:
    print("you didnt said anything!")

# this will make us to print the statement only if user enters something
# remember we said that empty strings are inherently false
# so the if condition will get triggered only when animal is non empty

# similarly empty object, empty string, zero and None are false by default
