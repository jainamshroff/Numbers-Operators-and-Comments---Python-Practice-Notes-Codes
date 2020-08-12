"""
Variables are like containers
Store some data, pull it out later
They can hold all sorts of things
Like numbers, booleans and strings
(and a lot more that we will talk about later)


variable in python are like variable in mathematics:
it is a named symbol that holds a value

think of it as a jar with label on it that says what is in it
and the content inside the jar is the content of the variable

FORM:
variablename = valueofthevariable
"""

x = 100
khaleesi_mother_of_dragons = 1

print(khaleesi_mother_of_dragons + x)

"""

most of the time our data keep changing and it is hard to keep track manually
thus we manipulate the variable and use the variable instead

variables are always assigned with variable name on the left and variable 
value on the right with a single equal to between them(assignment operator)

variable needs to be assigned before they can be used further

"""

num_of_cats = 99
print(num_of_cats * 2)

# but still the value of variable num_of_cat is 99 still
# what we are doing is give me value of num_of_cat and multiply it by 2 and print it
# but we can also change the variable value
# we can reassign the variable

friends = 0

num_of_cats = num_of_cats * 2
print(num_of_cats)
num_of_cats = 98
print(num_of_cats)
num_of_cats = num_of_cats - 1
print(num_of_cats)
friends = num_of_cats
print(friends)

# now the value of num_of_cats is changed itself

# we can also assign multiple variable at once

all, at, once = 5, 10, 15
# do this only when it makes sense, and they have something to do with them together

print(all)
print(at)
print(once)