#Class
#instand, Instance variable , class variable

class Dog :

    def __init__(self, namez):
        self.name = namez     #instance variable for each instance created
        # print ("Kutra1")

    def bark(self):
        print (f"Bhow!! {self.name}")   #this works well

class Bulldog (Dog):
    def intro(self):                    #This becomes the Class function that inherits the __init__ of Dog
        print (f"Bulldog!! {self.name}")

dog1 = Dog("Tommy")
print (dog1.name)
# print (dog1.bark())
dog1.bark()

dog2 = Dog("Halkat")
dog2.bark()
# dog1.name = "Tommy"
#
#
# dog2 = Dog()
# dog2.name = "Halkat"
# print (dog2.name)

dog3 = Bulldog("Chuti")
dog3.intro()

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def age(self):
        return(2025-self.year)


class Mustang(Car):
    def __init__(self, year):
        self.year = year
        super().__init__(self.year, "Ford", "Mustang")

my_car = Car(2015,"Honda", "Civic")
print(my_car.age())

new_car = Mustang(2022)
print (f"Details of car {new_car.make}, {new_car.model} bought in {new_car.year} is now {new_car.age()} old")