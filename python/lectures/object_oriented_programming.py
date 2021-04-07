class CoffeeM:
    # function that creates the instance of the object
    #this is a contructor fujnction or initializer
    def __init__(self, name):
        self.name = name
        self.water_temp = 200
        self.grind_size = 4
        self.milk_temp = 151
        self.brew_length = 7
        print(self)
        #first parameter in class function must be self
    def __init__(self):
        print(self.name)
#theis calls the __init__ function
mr_coffee = CoffeeM("Mr. Coffee")

mr_coffee.printInfo()

#polymorphsm
class CappucinoM( CoffeeM ):
    def __init__(self,name):
        super.__init__(name)
        self.milk = "whole"
    def make_cappucino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning froth!")

#abstraction
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def noise(self):
        print("I am an animal")
