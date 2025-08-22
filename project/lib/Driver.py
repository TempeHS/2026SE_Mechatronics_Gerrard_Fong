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
        #Finalised code
        while True:
            if self.__wheels.stopping():
                break
            self.__wheels.movingforward()
            self.__wheels.turningright()
            self.__wheels.turningleft()
            self.__RGBSensor.showgreen()

    def testing(self):
        #Testing values
        while True:
            self.__wheels.movingforward()
            self.__wheels.stopping()
            self.__wheels.turningleft()
            self.__wheels.turningright()
            self.__RGBSensor.showgreen()

FinalAct = SafetyRobot()

FinalAct.activate()
#Is this a tuff final name for the function