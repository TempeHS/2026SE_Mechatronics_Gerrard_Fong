from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

#This is the altercated version of the class that I used to properly unit test
#Changed the class name to prevent issues with my class calling and assocations later on
#Currently this version has no proper functionality

class LCDScreen...():
    def __init__(self):
        self.__display = create_PiicoDev_SSD1306()
        
    def displaying(self):
        #Asks for user input to properly test LCDScreen and variables
        thing = input("What's your name? ")
        self.__display.fill(0)
        self.__display.text("Name: ", 0, 20, 1)
        self.__display.text(thing, 0, 40, 1)
        self.__display.show()
        
