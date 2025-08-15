from machine import Pin, PWM
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from Movement import Wheels

class Ultrasonic():
    def __init__(self, range_a: list[int], range_b: list[int]):
        self.__range_front = PiicoDev_Ultrasonic(id=range_a)
        self.__range_side = PiicoDev_Ultrasonic(id=range_b)

    def distance(self):
        return self.__range_front.distance_mm, self.__range_side.distance_mm

    def idmove(self):
        if self.__range_front.distance_mm >= 300 and self.__range_side.distance_mm >= 40:
            return True
        else:
            pass
    
    def idstop(self):
        if self.__range_front.distance_mm < 90 and self.__range_side.distance_mm < 20:
            return True
        else:
            pass

    def idturnright(self):
        if self.__range_front.distance_mm < 100 and self.__range_side.distance_mm > 20:
            return True
        else: 
            pass
    
    def idturnleft(self):
        if self.__range_front.distance_mm < 100 and self.__range_side.distance_mm < 20:
            return True
        else: 
            pass