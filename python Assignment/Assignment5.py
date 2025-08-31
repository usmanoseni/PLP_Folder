# First task
# code that helps to create a car class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The car {self.make} {self.model} is now driving.")

    def reverse(self):
        print(f"The car {self.make} {self.model} is now reversing.")


class NewCar(Car):
    def __init__(self, make, model, year, country):
        super().__init__(make, model, year)
        self.country = country

    def showCountry(self):
        print(
            f"The car {self.make} {self.model} is manufactured in {self.country}.")


class oldCar(Car):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def show_mileage(self):
        print(
            f"The car {self.make} {self.model} has a mileage of {self.mileage} miles.")


my_car = Car("Toyota", "Camry", 2020)
my_car.drive()
my_car.reverse()

new_car = NewCar("Honda", "Civic", 2021, "Japan")
new_car.showCountry()

old_car = oldCar("Ford", "Mustang", 2015, 60000)
old_car.show_mileage()


# second tasks
# cod eon polymorphism
class Animal:
    def walk(self):
        print("All  animal has they way of walking")


class Dog(Animal):
    def walk(self):
        print("Dog walks on 4 legs")


class Bird(Animal):
    def walk(self):
        print("Bird walks on 2 legs")


class Fish(Animal):
    def walk(self):
        print("Fish swims in water")


WayOfWalking = [Dog(), Bird(), Fish()]

for animal in WayOfWalking:
    animal.walk()
