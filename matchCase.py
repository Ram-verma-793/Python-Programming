# The match case in python programming is similar to the switch case statement in java or c++ languages.

day = int(input("Enter day to check: "))
match day: 
    case 1 : print("It's sunday.")
    case 2 : print("It's monday.")
    case 3 : print("It's tuesday.")
    case 4 : print("It's wednesday.")
    case 5 : print("It's Thursday.")
    case 6 : print("It's friday.")
    case 7 : print("It's saturday.")
    case _ : print("invalid input.")