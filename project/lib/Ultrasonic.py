from machine import Pin, PWM
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from Movement import Wheels

class Ultrasonic():
    def __init__(self, range_a: list[int], range_b: list[int]):
        #Once again used Thribhu's class as a template to create the variables for class
        self.__range_front = PiicoDev_Ultrasonic(id=range_a)
        self.__range_side = PiicoDev_Ultrasonic(id=range_b)

    def distance(self):
        #A function made purely for visual error catching and making sure that the sensors work
        return self.__range_front.distance_mm, self.__range_side.distance_mm
        

    def idmove(self):
        #Technically a state machine method of identifying distances, may over complicate controller but oh well :|
        if self.__range_front.distance_mm >= 120:
            return True
            #The functions pure purpose is to only identify the robots options, thus the name of the function
            #I did this since I had no clue what else to do, might accidentally have a bunch of if chains when creating my driver
            #But that's an issue for another day
        else:
            pass
    
    def idstop(self):
        if self.__range_front.distance_mm <= 30 and self.__range_side.distance_mm < 30:
            return True
        #Identifies stopping range
        else:
            pass

    def idturnright(self):
        if self.__range_front.distance_mm < 40 and self.__range_side.distance_mm > 120:
            return True
        #Identifies safe range for turning right
        else: 
            pass
    
    def idturnleft(self):
        if self.__range_front.distance_mm <= 40 and self.__range_side.distance_mm < 120:
            return True
        #Identifies safe range for turning left
        else: 
            pass