from time import sleep
from Movement import Wheels
from Ultrasonic import Ultrasonic
from LCDScreen import LCDScreen
from RGBSensor import RGBSensor
#Importing MINE, all of MY classes

class MovementSubsystem:
    #Merging Movement and Ultrasonic sensor functionality
    def __init__(self, range_front: list[int], range_side: list[int], rwheel_pin: int, lwheel_pin: int):
        #Did this one on my own still using other classes as templates
        self.__wheels = Wheels(rwheel_pin, lwheel_pin)
        self.__dist = Ultrasonic(range_front, range_side)
        #Assocation

    def movingforward(self):
        #State Machine :P
        if self.__dist.idmove():
            self.__wheels.forward()
        #Identifies if its safe to move forward, moves robot and returns state
        #Might delete return state and implement in drivers for code running purposes
    
    def turningright(self):
        if self.__dist.idturnright():
            self.__wheels.turnright()
        #Ids parameters, Moves robot, returns right turn state
        
    def turningleft(self):
        if self.__dist.idturnleft():
            self.__wheels.turnleft()
        #Same as right turn function, just left turn instead

    def stopping(self):
        if self.__dist.idstop():
            self.__wheels.stopping()
            print("Stopping Robot")
            sleep(1)
            return True
        return False
        #Might not have to use this, or might have to improve it's functionality
        #In case robot tries diving head first into a wall and breaks ultrasonic sensors

class RGBSubsystem:
    #Identifies Green and simply prints green on LCD screen
    def __init__(self):
        self.__sensor = RGBSensor()
        self.__screen = LCDScreen()
        self.__wheelies = Wheels(16, 20)
        #Assocation 
    
    def showgreen(self):
        if self.__sensor.colourgreen():
            self.__screen.displaygreen()
            self.__wheelies.stopping()
            sleep(4)
            self.__wheelies.forward()
            sleep(0.5)
            #Sleep is used so the robot stops moving
        else:
            self.__screen.display()
            #Since this will be in a while true loop don't want it flooding terminal or anything
            #Another reason why pass is also in the RGBSensor function  
