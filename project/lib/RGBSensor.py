from time import sleep
from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_VEML6040 import PiicoDev_VEML6040

class RGBSensor:
    def __init__(self):
        self.__sensor = PiicoDev_VEML6040()
        
        
    
    def colourgreen(self):

        RGBSensor = self.__sensor.readHSV()
        hue = RGBSensor["hue"]

        if 80 < hue and hue < 95:
            print("Green")
        else: 
            pass

