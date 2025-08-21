from Controller import MovementSubsystem, RGBSubsystem
from time import sleep

print("Starting Unit Test")
sleep(2)

wheels = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)
RGBSensor = RGBSubsystem()

