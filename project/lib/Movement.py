from machine import Pin, ADC, PWM
from time import sleep
from servo import Servo


class Wheels:
    def __init__(self, rwheel_pin: int, lwheel_pin: int):
        #Used Thribhu's method of object instantiation to create class
        self.__freq = 50
        self.__dead_zone = 1500
        self.__min_speed = 500
        self.__max_speed = 2300

        self.__rwheel_pwm = PWM(Pin(rwheel_pin))
        self.__lwheel_pwm = PWM(Pin(lwheel_pin))
        #Thribhu's method using variables to replace pin values
        

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
        #Creating wheel and identifying objects separately

    def forward(self):
        #Sets both wheels at an equal speed to move robot forward
        self.__lwheel.set_duty(1300)
        self.__rwheel.set_duty(1700)
        #Duty set low to create steady speed
        #For debugging purposes, "Whitebox testing"
    
    def stopping(self):
        #Stops robot
        self.__rwheel.set_duty(1500)
        self.__lwheel.set_duty(1500)
        #Simple Debug
        
    def turnleft(self):
        #Turns robot left
        self.__lwheel.set_duty(1350)
        self.__rwheel.set_duty(1350)
        sleep(2.2)
        #Timer is used to turn robot at a 90 degree angle, Guess and check
        self.__rwheel.stop()
        self.__lwheel.stop()
        #Exception catching making sure the robot doesn't overshoot after turning during unit tests, since I use the sleep function
        #Which may cause it to overshoot
    
    def turnright(self):
        #Turns robot right
        self.__lwheel.set_duty(1650)
        self.__rwheel.set_duty(1650)
        sleep(1.84)
        #Guess and check value, something with the duty values made it so 1400 
        #would also stop robot thus the change in time and duty values
        self.__rwheel.stop()
        self.__lwheel.stop()
        

wheels = Wheels(16,20)

wheels.turnright()
sleep(1)
wheels.turnleft()

