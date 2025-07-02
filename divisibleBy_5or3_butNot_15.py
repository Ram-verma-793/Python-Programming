# Take positive integer and tell if it is divisible by 5 or 3 but not divisible by 15

num = int(input("Enter a positive integer. : "))

if num % 15 == 0:
    print(num, " is divisible by 15.")
else :
    if num % 3 == 0 or num % 5 == 0 :
        print(num, " is divisible by 3 or 5, but not divisible by 15.")
    else : print(num, " is neither divisible by 3 nor by 5.")