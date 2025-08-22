from Controller import RGBSubsystem
from Movement import Wheels

RGBSensor = RGBSubsystem()
Wheels = Wheels(16, 20)

while True:
    Wheels.turnright()