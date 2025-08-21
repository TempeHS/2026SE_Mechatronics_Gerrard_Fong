from Controller import MovementSubsystem, RGBSubsystem
from time import sleep

wheels = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)
RGBSensor = RGBSubsystem()

print("Starting Unit Test")
sleep(2)

while True:
    #This might just be the final code since the robot will run indefinitely
    wheels.movingforward()
    wheels.turningright()
    wheels.turningleft()
    if RGBSensor.showgreen():
        print("Green Found")
        wheels.stopping()
        #Realised this function may completely ruin functionality, so will only use for emergency situations in case of sensors breaking
        #Will also completely stop robot, unless I link it to left turn >: )
        break
        #End loop and unit test


