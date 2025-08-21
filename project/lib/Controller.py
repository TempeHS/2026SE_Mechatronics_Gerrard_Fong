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
            return "Moving_Forward"
        #Identifies if its safe to move forward, moves robot and returns state
    
    def turningright(self):
        if self.__dist.idturnright():
            self.__wheels.turnright()
            return "Turning_Right"
        #Ids parameters, Moves robot, returns right turn state
        
    def leftturn(self):
        if self.__dist.idturnleft():
            self.__wheels.turnleft()
            return "Turning_Left"
        #Same as right turn function, just left turn instead

    def stopping(self):
        if self.__dist.idstop():
            self.__wheels.stopping()
        #Might not have to use this, or might have to improve it's functionality
        #In case robot tries diving head first into a wall and breaks ultrasonic sensors

class RGBSubsystem:
    #Identifies Green and simply prints green on LCD screen
    def __init__(self):
        self.__sensor = RGBSensor()
        self.__screen = LCDScreen()
        self.__wheels = Wheels(16, 20)
        #Assocation 
        #Might be confusing that wheels variable is the same name as movement but idc
    
    def showgreen(self):
        if self.__sensor.colourgreen():
            self.__wheels.stopping()
            self.__screen.displaying()
            sleep(2)
            #Sleep is used so the robot stops moving
        else:
            pass
            #Since this will be in a while true loop don't want it flooding terminal or anything
            #Another reason why pass is also in the RGBSensor function  


