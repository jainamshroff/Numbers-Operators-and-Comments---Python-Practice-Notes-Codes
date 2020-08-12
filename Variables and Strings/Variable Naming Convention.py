"""
Variable naming restriction

it should start with a letter or a underscore
_cats is okay
2cats is not okay

The rest of the name must consist of letter, numbers or underscores
cats2 is okay
cats@2 is not okay

Names are case sensitive

CATS != cats
Cats != cats

it is extremly case sensitive

"""

cats2blahblahblah = 1
print(cats2blahblahblah)

# 2people = 344 # it throws the error invalid syntax because it should have started with a letter or a underscore
# jainam@gmail = 6 # again cannot name it like this
# jainam+gmail = 6 is also not possible


"""
Naming Convention

Snake Case

snake case - this_is_example_of_snake_case
camel case - thisIsExampleOfSnakeCase

variables should be lower case, it shouldn't be SNAKECASE

uppercase names are used for constants, the value of which do not change
all uppercase means it is a constant 

camel case are often used for classes 

__name__ followed by two underscores on both the side
they are called dunders and we should not mess with it 

snake case and lower case for variables 
camel case for classes
upper case for constants
two underscores on each side for dunders methods 


"""