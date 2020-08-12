# String Concatenation

# Adding Two Strings

message = "Hello World"
anothermessage = "I am Jainam"
resultstring = message + " " +anothermessage

print(resultstring)

username = "Jainam"
print("Hello there and welcome to the game, " + username)

# you cannot add integer with string

# print(8 + "character")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(str(8) + " " +"character")

guess = 10
print("your guess of " + str(guess) + " is wrong")

number = 1
number += 1 # same as number = number + 1
print(number)

stringvariable = "Hello"
stringvariable += " World"
print(stringvariable)