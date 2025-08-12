from machine import Pin, PWM
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

class Ultrasonic_Movement():
    def __init__(self):
        self.__range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.__range_b = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])

    def identifystop(self):
        if self.__range_a.distance_mm <= 400:
            return "slow"
        else:
            pass
    
    def identifyslow(self):
        if self.__range_a.distance_mm <= 200:
            return "stop"
        else:
            pass

distance = Ultrasonic_Movement()

while True:
    print(distance.identifystop)