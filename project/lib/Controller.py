from time import sleep
from Movement import Wheels
from Ultrasonic import Ultrasonic
from LCDScreen import LCDScreen
from RGBSensor import RGBSensor

class MovementSubsystem:
    def __init__(self, range_front: list[int], range_side: list[int], rwheel_pin: int, lwheel_pin: int):

        self.__wheels = Wheels(rwheel_pin, lwheel_pin)
        self.__dist = Ultrasonic(range_front, range_side)

    def forward(self):
        if self.__dist.idmove():
            self.__wheels.forward()
            return "1"
    
    def rightturn(self):
        if self.__dist.idturnright():
            self.__wheels.turnright()
            return "2"
    
    def leftturn(self):
        pass


class RGBSubsystem:
    def __init__(self):
        self.__sensor = RGBSensor()
        self.__screen = LCDScreen()
    
    def showgreen(self):
        if self.__sensor.colourgreen():
            self.__screen.displaying()
        else:
            pass


move = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)

print("Starting")
    
sleep(1)
