from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms


class LCDScreen():
    def __init__(self):
        self.__display = create_PiicoDev_SSD1306()

    def displaying(self):
        thing = "Green"
        self.__display.fill(0)
        self.__display.text("Colour: ", 0, 20, 1)
        self.__display.text(thing, 0, 40, 1)
        self.__display.show()

cal = LCDScreen()

cal.displaying()

