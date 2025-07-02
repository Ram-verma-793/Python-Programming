# Assign the grade of students on the marks
# if above 50 pass -> above 75 garde B -> above 90 grade A
#if less than 50 fail

result = float(input("Enter the marks of student: "))
if result > 50:
    if result >=90 : print("You got grade A.👌👌")
    elif result >=75 : print("You got grade B.😊")
    else : print("You got grade C.")
else : print("Better luck next time👍")