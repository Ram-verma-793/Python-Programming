english = float(input("Enter the marks of english: "))
maths = float(input("Enter the marks of maths: "))

# both above 80 is grade A
# one of them above 80 is grade B
# both less than 80 is grade C

if english > 80 and maths > 80 : print("Congrats you get grade A")
elif english > 80 or maths >80 : print("That's okay you get grade B")
else : print("Oh no it's grade C")