from time import sleep
from Movement import Wheels
from Ultrasonic import Ultrasonic

class MovementSubsystem:
    def __init__(self, range_front: list[int], range_side: list[int], rwheel_pin: int, lwheel_pin: int):

        self.__wheels = Wheels(rwheel_pin, lwheel_pin)
        self.__dist = Ultrasonic(range_front, range_side)

    def forward(self):
        while True:
            print(self.__dist.distance())
            if self.__dist.idturnright():
                self.__wheels.stopping()
                self.__wheels.turnright()
                sleep(1)

move = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)

print("Starting")
sleep(1)
move.forward()