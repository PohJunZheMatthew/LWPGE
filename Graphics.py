"""
Author: Matthew Poh
A simple, lightweight library that can do basic graphics stuff
"""
from pybricks.hubs import *
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import *
from umath import *
from Exceptions import *
class Point():
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def __str__(self):
        return f"new Point({self.x},{self.y})"
class Line():
    def __init__(self,point1:Point,point2:Point,brightness:int):
        self.point1 = point1;
        self.point2 = point2;
        if brightness > 100 or brightness < 0:
            raise brightnessOutOfBounds
        else:
            self.brightness = brightness
    def getPoint1():
        return self.point1
    def getPoint1():
        return self.point1
class Shape():
    def __init__(self,x:int,y:int,shapeArray):
        """
        ShapeArray is an array containing a lot of array which contains the brightness value for the graphics class to draw it out on to the primehub's display.
        ShapeArray example: 
        ┌              ┐ 
        │[100,100,100],│
        │[100,000,100],│
        │[100,000,100],│
        │[100,100,100] │
        └              ┘
        //The result should be 3x4 square with two square missing at the center
        """
        try:
            for xArrays in shapeArray:
                for brightness in xArrays:
                    if brightness > 100 or brightness < 0:
                        raise brightnessOutOfBounds
        except(error):
            raise failedToInitializationShape
        else:
            self.shapeArray
            self.x = x
            self.y = y
class Rect():
    def __init__(self,x:int,y:int,width:int,height:int,brightness=100):
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        if brightness > 100 or brightness < 0:
            raise brightnessOutOfBounds
        else:
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
class TextMotionType:
    none = 0
    fromTheRight = 1
    fromTheLeft = 2
    fromTheTop = 3
    fromTheBottom = 4
    absolute = 5
    fixed = 5
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
        #Fills the screen with the desired brightness
        for i in range(5):
            for o in range(5):
                PrimeHub().display.pixel(i,o,brightness)
    def drawLine(self,line:Line):
        width = line.point2.x-line.point1.x
        height = line.point2.y-line.point1.y
        RadAngle = atan2(float(height),float(width))
        for i in range(100):
            loopingPercent = i/width
            y = line.point1.y+height*loopingPercent
            x = line.point1.x+width*loopingPercent
            PrimeHub().display.pixel(int(x),int(y),line.brightness)
    def drawShape(self,shape:Shape):
        x = shape.x
        y = shape.y
        for yoffset,arrays in enumerate(shape.shapeArray):
            for i,brightness in enumerate(arrays):
                PrimeHub().display.pixel(x+i,y+yoffset,brightness)
    def Clock(self,frameRate:int):
        wait(1000/frameRate)
    def Refresh(self):
        #clear the screen such that other components can be drawed on it
        for i in range(5):
            for o in range(5):
                PrimeHub().display.pixel(i,o,0)
    def drawString(self,string:str,textMotionType:int=0,textSpacing:int=2,spaceSpacing:int=4):
        #Still developing the drawString func 
        pass
