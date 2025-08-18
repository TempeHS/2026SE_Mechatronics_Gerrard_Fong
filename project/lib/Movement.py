from machine import Pin, ADC, PWM
from time import sleep
from servo import Servo

class Wheels:
    def __init__(self, rwheel_pin: int, lwheel_pin: int):
        #Used Co-Pilot to understand what to instantiate
        self.__freq = 50
        self.__dead_zone = 1500
        self.__min_speed = 500
        self.__max_speed = 2300
        self.__current_speed = 0

        self.__rwheel_pwm = PWM(Pin(rwheel_pin))
        self.__lwheel_pwm = PWM(Pin(lwheel_pin))
        #configure pins later
        

        self.__rwheel = Servo(
            pwm = self.__rwheel_pwm,
            freq = self.__freq,
            min_us = self.__min_speed,
            max_us = self.__max_speed,
            dead_zone_us = self.__dead_zone)
        
        self.__lwheel = Servo(
            pwm = self.__lwheel_pwm,
            freq = self.__freq,
            min_us = self.__min_speed,
            max_us = self.__max_speed,
            dead_zone_us = self.__dead_zone)

    def forward(self):
        self.__lwheel.set_duty(1300)
        self.__rwheel.set_duty(1700)
        print("Moving")
    
    def stopping(self):
        self.__rwheel.set_duty(1500)
        self.__lwheel.set_duty(1500)
        print("Stopped")
        
    def turnleft(self):
        self.__lwheel.set_duty(1350)
        self.__rwheel.set_duty(1350)
        print("Turning left")
        sleep(1.7)
        self.__rwheel.stop()
        self.__lwheel.stop()
    
    def turnright(self):
        self.__lwheel.set_duty(1600)
        self.__rwheel.set_duty(1600)
        print("Turning right")
        sleep(3.147)
        self.__rwheel.stop()
        self.__lwheel.stop()
        

wheels = Wheels(16,20)

wheels.turnleft()


