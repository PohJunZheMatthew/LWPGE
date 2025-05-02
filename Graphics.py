from pybricks.hubs import *
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import *
"""
Author:Matthew Poh
"""
class Point():
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def __str__(self):
        return f"new Point({self.x},{self.y})"
class Rect():
    def __init__(self,x:int,y:int,width:int,height:int,brightness=100):
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.brightness = brightness
    def getPos(self):
        return Point(self.x,self.y)
    def getSize(self):
        return [self.width,self.height]
    def getBrightness(self):
        return self.brightness
    def setPos(self,x,y):
        self.x = x
        self.y = y
    def setSize(self,width,height):
        self.width = width;
        self.height = height;
    def contains(self,point:Point):
        if (point >= self.x) and (point <= self.x+self.width) and (point >= self.y) and (point <= self.y+self.height):
            return True
    def __str__(self):
        return f"new Rectangle[x={self.x}, y={self.y}, width={self.width}, height={self.height}, brightness={self.brightness}]"
class Graphics():
    def fillRect(self,rect:Rect):
        for i in range(rect.width):
            for o in range(rect.height):
                PrimeHub().display.pixel(rect.x+i,rect.y+o,100)
    def drawRect(self,rect:Rect):
        for num in range(2):
            for i in range(rect.width):
                PrimeHub().display.pixel(rect.x+i,rect.y+(rect.height*num),100)
            for i in range(rect.height):
                PrimeHub().display.pixel(rect.x+i,rect.y+(rect.height*num),100)
    def fillScreen(self,brightness:int):
        for i in range(5):
            for o in range(5):
                PrimeHub().display.pixel(i,o,brightness)
    def Clock(self,frameRate:int):
        wait(1000/frameRate)
    def Refresh(self):
        for i in range(5):
            for o in range(5):
                PrimeHub().display.pixel(i,o,0)
