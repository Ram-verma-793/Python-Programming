class Car:
    def __init__(self):
        self.name = None
        self.color = None
        self.type = None

    def run(self):
        print("The car have running capacity.")

class tata(Car):
    def build(self):
        print("The tata cars have solid build.!")


c1 = tata()
c1.name = "Safari"
c1.color = "red"
c1.type = "family"
print(c1.name)
print(c1.color)
print(c1.type)
c1.build()
c1.run()
