class Rectangle:
    def set_dimensions(self):
        self.height = int(input("Enter the height of the Rectangle: "))
        self.width  = int(input("Enter the width of the Rectangle: "))


    def area(self):
            return self.height * self.width

    def perimeter(self):
            return 2 * (self.height + self.width)


    def checkSquare(self):
          if self.height == self.width:
                print("It's a square.")
          else: print("It's not a square!")      


# creating the object 
rect = Rectangle()
rect.set_dimensions()



print("\n1. Area  2. perimeter  3. Check Square or Not  4. Exit  :: ")
choice = int(input("Enter a choice you want: "))
match choice:
            case 1: print("Area of the Rectangle is: ", rect.area())
            case 2: print("Perimeter of the Rectangle is: ", rect.perimeter())
            case 3: rect.checkSquare()
            case 4: print("Exiting the program..")
        
            case _: print("wrong choice!")
      
