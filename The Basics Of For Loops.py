# 'for' Loops
# used on something that we can iterate over or loop through
# example: string or list or number in this range

"""
Syntax

for item in iterable_object:
    # do somethng with item

iterable_objects are nothing but collection of data
item is a new variable that can be called whatever you want
item references the current position of our iterator within the iterable.
It will iterate over every item of the collection and then go away when it has
visited all the items

"""

# item represent the current item in the iterable objects that we are iterating over RN
for item in "Hello":
    print(item,end="")

print("\n")
for number in range(1, 8):
    print(number,end="")

# range has two limits the starting is included but the end limit is not
# so our range of  1 - 8 is including 1 but not including 8
print("\n")
for i in range(1, 10):
    print(i, end="")

for letter in "coffee":
    print(letter * 10)

# we can multiply the string while printing and it will print that many times
# but it will work only for strings and not for numbers as it will multiply with the number itself


