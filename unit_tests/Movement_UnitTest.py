from time import sleep
from Movement import Wheels


sleep(2)

wheels = Wheels(16,20)
#Create variable for class before starting unit test

print("Start Movement Unit Test")

wheels.stopping()
#Make sure wheels aren't moving before starting test
sleep(2)

wheels.forward()
print("Moving forward")
sleep(5)

wheels.stopping()
print("Stopping movement")
sleep(5)

wheels.turnright()
print("Turning right")
wheels.stopping()
#Didn't use sleep functions after turns as I found out it overshot the turn
#Will implement new functionality to turning functions to prevent this

print("Turning left")
wheels.turnleft()

wheels.stopping()
print("Unit Test Complete")
#End of unit test
