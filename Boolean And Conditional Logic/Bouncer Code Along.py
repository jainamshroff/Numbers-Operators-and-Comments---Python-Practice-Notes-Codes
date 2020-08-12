"""

Ask for age

18 - 21 wristband
21 + drink, normal entry
too young, sorry

"""

age = int(input("How old are you: "))

if age != "":
    if age >= 18 and age <=21:
        print("You can enter but you need a wristband!")
    elif age > 21:
        print("You can enter and have a drink !")
    elif age < 18:
        print("Too Young Can't Enter")
    else:
        print("Enter a Valid Input")
else:
    print("Enter a Input First!")