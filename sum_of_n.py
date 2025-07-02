def sumOf_n(n) : 
    sum = 0
    for i in range(1, int(n)+1):
        sum += i
    print("The sum of ",n, " numbers is: ", sum)

n = float(input("Enter the value of n: "))
sumOf_n(n) 