'''
Description:

Write a simple function that takes polar coordinates (an angle in degrees and a radius) and returns the equivalent cartesian coordinates (rouded to 10 places).

For example:

coordinates(90,1)
=> (0.0, 1.0)

coordinates(45, 1)
=> (0.7071067812, 0.7071067812)
'''


##########MY SOLUTION##########
import math

def coordinates(degrees, radius):
    x = round(radius*math.cos(math.radians(degrees)),10)
    y = round(radius*math.sin(math.radians(degrees)),10)
    return (x,y)