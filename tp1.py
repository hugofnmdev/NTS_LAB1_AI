from utils import *
from rng import *
from math import *

rng = 1


def midpoint(p1,p2):
    """
    @param p1 couple of integers
    @param p2 couple of integers
    @return the middle of the segment p1p2, as a couple of integers ! 
    """
    return ((p1[0]+p2[0])//2,(p1[1]+p2[1])//2)


def midpoint_displacement(l, delta, dh, base_height):
    """
    @param l list of points
    @param delta the threshold as defined in the subject
    @param dh the parameter defining the variation of height at a step of the midpoint displacement algorithm
    @param baseheight the minimum height of all coordinates (important for drawing)
    @return the list containing the points after midpoint displacement
    """
    

def generateMountain(window_width, base_height, min_width, max_width, min_height, max_height):
    """
    @param window_width the width of the windows where all will be drawn
    @param base_height the minimum height of all coordinates (important for drawing)
           note that the base of the mountain should be at this height
    @param min_width the minimum width of the base of the mountain
    @param max_width the maximum width of the base of the mountain
    @param min_height the minimum height of the mountain
    @param max_height the maximum height of the mountain
    @return a list of couple of integers defining the mountain, where two successive points are a segment
    """
    pass
    
def generateMountains(n, window_width, baseheight, min_width, max_width, min_height, max_height):
    """
    @param n the number of mountains
    @param window_width the width of the windows where all will be drawn
    @param base_height the minimum height of all coordinates (important for drawing)
           note that the base of the mountain should be at this height
    @param min_width the minimum width of the base of the mountain
    @param max_width the maximum width of the base of the mountain
    @param min_height the minimum height of the mountain
    @param max_height the maximum height of the mountain
    @return a list of list of couple of integers defining the mountain, where two successive points are a segment (ie list of mountains)
    """
    return [generateMountain(window_width, baseheight, min_width, max_width, min_height, max_height) for i in range(n)]

###### Partie 2

def generation(axiom, rules, n):
    """
    axiom the initial string
    rules the set of rules, given as pairs (keys,values) in a dictionary
    n the number of iterations
    """
    

def plant0():
    axiom='F'
    rules={'F':'F[+F]F[-F]F'}
    angleL, angleR, angle0 = 20., -20., 90.    
    return axiom, rules, angleL, angleR, angle0
    
def plant1():
    axiom='F'
    rules={'F':'F[+F]F[-F][F]'}
    angleL, angleR, angle0 = 25.7, -25.7, 90.    
    return axiom, rules, angleL, angleR, angle0
    
def plant2():
    axiom='F'
    rules={'F':'FF-[-F+F+F]+[+F-F-F]'}
    angleL, angleR, angle0 = 22.5, -22.5, 90.    
    return axiom, rules, angleL, angleR, angle0
    
def plant3():
    axiom='X'
    rules={'X':'F[+X]F[-X]+X','F':'FF'}
    angleL, angleR, angle0 = 20.0, -20.0, 90.    
    return axiom, rules, angleL, angleR, angle0
    
def plant4():
    axiom='X'
    rules={'X':'F[+X][-X]FX','F':'FF'}
    angleL, angleR, angle0 = 25.7, -25.7, 90.    
    return axiom, rules, angleL, angleR, angle0
    
def plant5():
    axiom='X'
    rules={'X':'F-[[X]+X]+F[+FX]-X','F':'FF'}
    angleL, angleR, angle0 = 22.5, -22.5, 90.    
    return axiom, rules, angleL, angleR, angle0


def new_position(posX,posY,angle,distance):
    """
    @param posX the initial x position
    @param posY the initial y position
    @param angle the angle with the Ox axis
    @param distance the distance of the move
    @return a couple of integers that are the new position
    """
    pass
 
def string_to_lines(string, posX, posY, initial_angle, angleL, angleR, distance):
    """
    @param string the string given by applying the rewriting rules to the axiom
    @param posX the initial x position
    @param posY the initial y position
    @param initial_angle the initial angle
    @param angleL the angle for left turns (signed)
    @param angleR the angle for right turns (signed)
    @param distance the size of the segments
    @return a list of couples of couples of integers ((x1,y1),(x2,y2))$, that are the segments to draw
    """
    pass
