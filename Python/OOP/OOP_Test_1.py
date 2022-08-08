# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Déclaration class Point
class Point:
    # Constructeur utilisé automatiquement à l'initialisation instance
    def __init__(self, x, y): 
        self.x = x      # Déclaration public
        self.__y = y    # Déclaration private avec __
        
    def PrintValueXY(self):
        print("x ", p.x)
        print("y ", p.__y)
        
    def SetY(self,y):
        self.__y = y

# Initialisation instances
p = Point(1,2)

p.PrintValueXY()


p.x = 789
p.__y = 123

p.PrintValueXY()

p.SetY(456)

p.PrintValueXY()

