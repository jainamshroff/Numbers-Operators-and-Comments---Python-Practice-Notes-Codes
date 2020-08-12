"""

Logical AND and OR - called logical operators

and Truthy when a AND b both are True - if a and b:
                                            print(c)
or Truthy when either a OR b are True - if tired or bedtime:
                                            print(go sleep)
not Truthy if opposite of a is True - if not weekend:
                                            print(go work)

"""

# Movie ticket example
# 0 - 2 free
# 2 - 8 child ticket
# 10 above regular ticket

age = int(input())

if age > 2 and age < 8:
    print("Child Ticket")