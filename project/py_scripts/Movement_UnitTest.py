from time import sleep
from Movement import Wheels


print("Hello world")

sleep(2)

wheels = Wheels(16,20)

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

print("Turning left")
wheels.turnleft()

wheels.stopping()
print("Unit Test Complete")
