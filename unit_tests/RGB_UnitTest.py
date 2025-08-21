from time import sleep
from RGBSensor import RGBSensor

#Tests Colour Sensor class

colour = RGBSensor()

while True:
    #Constantly calls function and senses for colour green
    #Originally had another print function that would identify whether green was there or not
    #Removed for programming purposes and stop flooding of terminal for finalisation of code
    colour.colourgreentest()