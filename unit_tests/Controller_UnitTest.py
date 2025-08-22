from Controller import MovementSubsystem, RGBSubsystem
from time import sleep

wheels = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)
RGBSensor = RGBSubsystem()

print("Starting Unit Test")
sleep(2)

while True:
    #This might just be the final code since the robot will run indefinitely
    if wheels.stopping():
        break
    #End loop and unit test
    wheels.movingforward()
    wheels.turningright()
    wheels.turningleft()
    RGBSensor.showgreen()
        


