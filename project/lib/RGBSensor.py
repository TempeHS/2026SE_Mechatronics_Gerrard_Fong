from time import sleep
from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_VEML6040 import PiicoDev_VEML6040
#Importing Colour sensor modules


class RGBSensor:
    def __init__(self):
        self.__sensor = PiicoDev_VEML6040()
        #Define specific sensor, since there were two used examples to help
        
    
    def colourgreen(self):
        RGBSensor = self.__sensor.readHSV()
        hue = RGBSensor["hue"]
        #Used example code as a foundation
        if 80 < hue and hue < 95:
            print("Green")
        #Identify if colour sensor detects green and prints Green,
        #Might change later when integrating into subsystem
        else: 
            pass
        #Finishing function to prevent any errors in case if function is invalid during testing
        #Used to have another print function when unit testing

