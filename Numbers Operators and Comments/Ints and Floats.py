"""
Two main ways python represents numbers are:

- int
- float

- Some examples are:

    int     float
    4       6.1
    57      1.333333
    -10     0.0

The numbers with decimal potentially take much more space than non decimal numbers
actually that are four types of numbers - int, float, complex and long

Decimal number representation takes up much more work than the whole numbers.

All comes down to space

Integers - Whole numbers, positive or negative
Float Point Number - Numbers having decimal, positive or negative again

*** 1.0 is also an example of floating point number ***

*** Always Remember when you do math with int and float, python will give
float as the output or result ***

"""

# type(), we give it a number and it return the type of the number

print(type(9)) # it says the type is - <class 'int'>
print(type(9.0)) # it says the type is - <class 'float'>

print(1 + 3)   # since both the numbers are int output will be int
print(1 + 1.0) # Rather than just 2 it gives output as 2.0

# when we add int with a float it will give float as output
# when you do math with int and float python will give float as output
