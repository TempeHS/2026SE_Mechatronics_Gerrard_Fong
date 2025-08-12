from time import sleep
from Movement.py import Wheels


print("Hello world")

sleep(2)

wheels = Wheels(16,20)

print("Start Movement Unit Test")

wheels.stop()
#Make sure wheels aren't moving before starting test
sleep(2)

wheels.forward()
print("Moving forward")
sleep(5)

wheels.stop()
print("Stopping movement")
sleep(10)

wheels.turnright()
print("Turning right")


wheels.stop()
print("Unit Test Complete")
