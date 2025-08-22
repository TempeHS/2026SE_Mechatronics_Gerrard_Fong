from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
#Imported modules from example, no clue what "*" does, assuming it acts as a placeholder


class LCDScreen():
    #Create class
    def __init__(self):
        self.__display = create_PiicoDev_SSD1306()
        #Set value for display screen
    def displaygreen(self):
        #A simple function that will display green on LCD screen will be integrated later for practical functionality
        
        self.__display.fill(0)
        self.__display.text("Colour: ", 0, 20, 1)
        self.__display.text("Green", 0, 40, 1)
        self.__display.show()
        #Used code from example

    def display(self):
        self.__display.fill(0)
        self.__display.text("No Green Found ", 0, 20, 1)
        self.__display.show()
        #Used code from example

    def displaytest(self):
        #Function for unit testing
        #Asks for user input to properly test LCDScreen and variables
        thing = input("What's your name? ")
        self.__display.fill(0)
        self.__display.text("Name: ", 0, 20, 1)
        self.__display.text(thing, 0, 40, 1)
        self.__display.show()
        