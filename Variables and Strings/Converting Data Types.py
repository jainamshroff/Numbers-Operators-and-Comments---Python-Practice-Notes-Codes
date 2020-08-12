# Converting Data Types

stringnumber = "100"
print(type(stringnumber))
stringnumber = int(stringnumber)
print(type(stringnumber))
stringnumber = float(stringnumber)
print(type(stringnumber))
stringnumber = str(stringnumber)
print(type(stringnumber))

decimalvariable = 12.5666777
decimalvariable = int(decimalvariable)
print(decimalvariable)

list = [1, 2, 3]
list = str(list)
print(list)

# when we are interpolating things are implicitly getting converted
# to string behind the scenes, to do it explicitly it is shown above