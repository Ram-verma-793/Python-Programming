class Father:
    def name(self):
        print("The family has father's name before own name.")

class Mother:
    def love(self):
        print("The child have loving nature!")

class child(Father, Mother):
    def play(self):
        print("The child have playing nature.!")


# creating object

c1 = child()
c1.name()
c1.love()
c1.play()