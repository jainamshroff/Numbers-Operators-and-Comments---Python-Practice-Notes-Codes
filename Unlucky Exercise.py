

for number in range(1, 21):
    print(number)
    if number == 4 or number == 13:
        print("unlucky")
    elif number % 2 == 0:
        print("Even")
    else:
        print("Odd")
