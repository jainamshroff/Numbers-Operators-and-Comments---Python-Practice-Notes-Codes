"""

Weird Operators

- Exponentiation
- Symbol - "**" - exponentiation
- 2 ** 3 means 2^3

- Modulo
- Symbol - "%" - remainder operator
- 11 % 2 means what will be the remainder when 11 is divided by 2
- so here 2 times 5 is 10 and 1 will be the remainder thus 1 will be our answer
- 10 % 2 will be 0 as 2 times 5 is 10 and nothing is left as remainder

-Integer Division
- Symbol - "//" -  Integer Division
- 10 / 3 gives us 3.33333, but what if we do not want the decimal part
- 10//3 gives us 3 as result, it chops off all the decimal part and returns only integer
- 10//3 = 3 rather than 3.333333

"""

print(2 ** 3) # exponent
print(11 % 2) # modulo/remainder operator
print(10/2) # we know that python gives float in return
print(10 // 3) # it gives out only integer, it chops out the decimal part
                # 3.3333 should be the answer but .3333 will be chopped
