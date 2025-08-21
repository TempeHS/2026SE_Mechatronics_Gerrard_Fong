from Controller import MovementSubsystem, RGBSubsystem
from time import sleep

wheels = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)
RGBSensor = RGBSubsystem()

print("Starting Unit Test")
sleep(2)

while True:
    wheels.
