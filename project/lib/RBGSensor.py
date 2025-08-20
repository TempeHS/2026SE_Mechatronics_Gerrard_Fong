from time import sleep
from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_VEML6040 import PiicoDev_VEML6040

class RGBSensor:
    def __init__(self):
        self.__sensor = PiicoDev_VEML6040()
        self.__RGBSensor = self.__sensor.readHSV()
        self.__hue = self.__RGBSensor["Hue"]
        
    
    def colourgreen(self):
        if 80 < self.__hue  and self.__hue < 95:
            print("Green")
        else: 
            print("Yo no green")

colour = RGBSensor()

while True:
    colour.colourgreen()