from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch,multitask, run_task
def getAllPressedHubButtons():
    btns = {Button.BLUETOOTH:{Button.BLUETOOTH in PrimeHub().buttons.pressed()},Button.CENTER:(Button.CENTER in PrimeHub().buttons.pressed()),Button.LEFT:(Button.LEFT in PrimeHub().buttons.pressed()),Button.RIGHT:(Button.RIGHT in PrimeHub().buttons.pressed())}
    return btns
def checkIfButtonIsPressed(btn):
    return btn in PrimeHub().buttons.pressed()
def setCENTERButtonColor(btn,color:Color):
    PrimeHub().light.on(color)
