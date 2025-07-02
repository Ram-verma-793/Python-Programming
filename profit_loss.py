cost = int(input("Enter the cost price: "))
sell = int(input("Enter the selling price: "))

if cost < sell : print("Making profit of", sell-cost)
elif cost == sell : print("It's the same cost and sell")
else : print("You're in loss of :", cost-sell)