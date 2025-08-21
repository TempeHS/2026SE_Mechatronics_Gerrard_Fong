from Controller import MovementSubsystem, RGBSubsystem
from time import sleep

#Checked the Traffic Light code realised it's essentially controller with a new name so, practically revamping controller here
#This is the final code

class SafetyRobot():
    def __init__(self):

        self.__wheels = MovementSubsystem([0, 0, 0, 0], [0, 0, 1, 0], 16, 20)
        self.__RGBSensor = RGBSubsystem()
        #Instaniate the big boy classes
    
    def activate(self):
        while True:
            self.__wheels.movingforward()
            #Starts robot movement
            if self.__wheels.movingforward() == "Moving_Forward":
                #Continue robots movement since it's obviously moving forward
                #Implemented for the sake of state machine implementation
                self.__wheels.turningright()
                self.__wheels.turningleft()
            else:
                self.__RGBSensor.showgreen()
                continue
            #If the robot can't turn keep looking for green and if not found keeping moving forward

    def testing(self):
        while True:
            self.__wheels.movingforward()
            self.__wheels.stopping()
            self.__wheels.turningleft()
            self.__wheels.turningright()
            self.__RGBSensor.showgreen()

FinalAct = SafetyRobot()

FinalAct.testing()
#Is this a tuff final name for the function