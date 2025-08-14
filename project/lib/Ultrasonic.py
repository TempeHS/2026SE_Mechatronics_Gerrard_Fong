from machine import Pin, PWM
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from Movement import Wheels

class Ultrasonic_Movement():
    def __init__(self, range_a: list[int], range_b: list[int]):
        self.__range_front = PiicoDev_Ultrasonic(id=range_a)
        self.__range_side = PiicoDev_Ultrasonic(id=range_b)

    def distance(self):
        return self.__range_front.distance_mm, self.__range_front.distance_mm

    def identifystop(self):
        if self.__range_front.distance_mm <= 400:
            return "slow"
        else:
            pass
    
    def identifyslow(self):
        if self.__range_front.distance_mm <= 200 and self.__range_side.distance_mm <= 200:
            return True
        else:
            print("gay")

wheels = Wheels(16, 20)
distance = Ultrasonic_Movement([0, 0, 0, 0], [0, 0, 1, 0])


while True:
    wheels.forward()
    distance.distance()
    if distance.identifyslow():
        wheels.turnright()
        break