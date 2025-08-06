from machine import Pin, PWM
from time import sleep
from servo import Servo

class Wheels(Pin, PWM):
    def __init__(self, rwheel, lwheel):
        #Used Co-Pilot to understand what to instantiate
        self.__freq = 50
        self.__dead_zone = 1500
        self.__min_speed = 500
        self.__max_speed = 2300

        self.__rwheel_pin = PWM(Pin(15))
        self.__lwheel_pin = PWM(Pin(16))
        #configure pins later


        self.__rwheel = Servo(
            pwm = self.__rwheel_pin,
            freq = self.__freq,
            min_us = self.__min_speed,
            max_us = self.__max_speed,
            dead_zone_us = self.__dead_zone) 
        
        self.__lwheel = Servo(
            pwm = self.__lwheel_pin,
            freq = self.__freq,
            min_us = self.__min_speed,
            max_us = self.__max_speed,
            dead_zone_us = self.__dead_zone) 
        
        self.__bothwheels = (self.__lwheel, self.__rwheel)
        #Fixed variable using Co-Pilot, was a tuple before with no actual functionality

    def forward(self):
        
    def backward():

    def turnleft():

    def turnright():

    def spin():

    def stop():



    
