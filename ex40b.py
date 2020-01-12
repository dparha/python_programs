#!/usr/bin/env python3

# class practice


class Car(object):

    speed = "slow"
    amount_of_cars = 0
    
    def __init__(self, size, name):
        self.size = size
        self.__name__ = name
        Car.amount_of_cars += 1
        
    def gas(self):
        if self.speed == "slow":
            self.speed = "medium"
            print(self.__name__, "is speeding up.")
        elif self.speed == "medium":
            self.speed = "fast"
            print(self.__name__, "is flying now!")
        elif self.speed == "stopped":
            self.speed = "slow"
            print(self.__name__, "is slowly cruising.")
        else:
            print(self.__name__, "is at top speed!")

    def brake(self):
        if self.speed == "slow":
            self.speed = "stopped"
            print(self.__name__, "pulled over and stopped.")
        elif self.speed == "medium":
            self.speed = "slow"
            print(self.__name__, "slowed to a crawl.")
        elif self.speed == "fast":
            self.speed = "medium"
            print(self.__name__, "eased up, but is still moving!")
        else:
            print(self.__name__, "already stopped.")

    def stop(self):
        if self.speed != "stopped":
            self.speed = "stopped"
            print(self.__name__, "screeched to a halt!")
        else:
            print(self.__name__, "is already stopped.")

            
ford = Car("midsize", "focus")
print(ford.amount_of_cars)

dodge = Car("compact", "charger")

print(dodge.amount_of_cars)

print(dodge.speed)
dodge.gas()
print(dodge.speed)
dodge.gas()
print(dodge.speed)
dodge.gas()
print(dodge.speed)
print(dodge.__name__)
dodge.stop()
print(dodge.speed)

porsche = Car("sedan", "boxter")
print(Car.amount_of_cars)
