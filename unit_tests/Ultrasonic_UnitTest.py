from Ultrasonic import Ultrasonic
from time import sleep

distance = Ultrasonic([0, 0, 0, 0], [0, 0, 1, 0])
#Connect class to a variable

print("Starting test")
sleep(2)

while True:
    #Constantly print distance, so I can catch any errors visually
    #Terminal will print one of the following terms depending on distance from sensor
    #Sometimes the terminal will flood with both distance and print statements but I didn't mind as long as it works : |
    print(distance.distance())
    if distance.idturnright():
        print("Turning right")
    elif distance.idturnleft():
        print("Turning Left")
    elif distance.idmove():
        print("Moving forward")
    elif distance.idstop():
        print("Stopping")
        break
        #Created this to properly end unit test and stop terminal flooding
    else:
        pass
    #Continues to print distances