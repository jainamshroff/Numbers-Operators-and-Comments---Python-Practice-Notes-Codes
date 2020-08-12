# Introduction to conditionals

"""

if some condition is True:
    do something - this will only run it that condition is true
elif some other condition is True:
    do something
else:
    do something

"""


print("Enter Name: ")
name = input()


if name == "Arya Stark":
    print("Valar Morghulis")

elif name == "Jon Snow":
    print("You Know Nothing")

else:
    print("Carry On")