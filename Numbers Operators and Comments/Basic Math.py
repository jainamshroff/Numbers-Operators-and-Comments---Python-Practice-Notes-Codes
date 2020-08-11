"""

Common Operators in python

    Symbol      Name
    +           Addition
    -           Subtraction
    *           Multiplication
    /           Division
    **          Exponentiation
    %           Modulo
    //          Integer Division

python always return float for division operation by default

"""

# Some Basic Maths Operations

print(1 + 3)  #output - int
print(4 - 1.0)  #output - float as one of the number is float
print(5 * 2)  #output - int
print(5 * 2.0)  #output - float as one of the number is float
print(4 / 2) #output - float in python division always return a float


"""
- The order of operations
- if we do something like 1 + 2 * 5 / 3
- we have something called operator precedence 
- PEMDAS - parentheses Exponents Multiplication Division Addition Subtraction
- we follow the PEMDAS mode of operation while solving a calculation
- which is same as real life maths 

- if you do something like (1 + 2) * 5 / 3, this time addition will be done first
- as parentheses are solved first.
"""