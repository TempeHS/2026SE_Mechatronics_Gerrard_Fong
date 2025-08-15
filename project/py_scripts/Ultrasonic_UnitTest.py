from Ultrasonic import Ultrasonic
from time import sleep

distance = Ultrasonic([0, 0, 0, 0], [0, 0, 1, 0])

print("Starting test")
sleep(2)

while True:
    print(distance.distance())
    if distance.idturnright():
        print("Turning right")
        break
    elif distance.idturnleft():
        print("Turning Left")
        break
    elif distance.idmove():
        print("Moving forward")
    elif distance.idstop():
        print("Stopping")
        break
    else:
        pass