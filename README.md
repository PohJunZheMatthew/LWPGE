# LWPGE
## About LWPGE:
L.W.P.G.E means Lightweight Pybricks Graphics library 
It is a lightweight graphic library that works on Pybricks.
It is currently going through its alpha stages and isn't completed yet.
It can be used to make games on the Prime's hub display.
## Contributors:
Currently, it is only I contributing, and I do not have a Spike Prime Hub at home, so I have to test some of the code in School.
## Tutorial and usage:
### 1. Create a gameloop:
1. Start by importing the necessary library and modules first
```
from pybricks import *
from LWPGE import *
```
2. Create the gameLoop
```
while True:
  Graphics.Clock(60)
  Graphics.Refresh()
```
Tip: Make sure you add `Graphics.Clock(60)` to have 60 fps to make sure it does not crash <br>
Tip: Make sure you add `Graphics.Refresh()` to clear the display and refresh it

And there we have it, our first GameLoop. It can now run at 60 fps.
### 2. Drawing objects to the screen:
Right now, our hub's display is blank and empty. We should draw some objects onto the display of the hub
Continuing from tutorial one
```
from pybricks import *
from LWPGE import *
while True:
  Graphics.Clock(60)
  Graphics.Refresh()
```
1. Start by creating our first rectangle:
Start by inserting this line of code:
`rect = Rect(1,1,2,2,100)`
So your code should look like this:
```
  from pybricks import *
  from LWPGE import *
  while True:
    rect = Rect(1,1,2,2,100)
    Graphics.Clock(60)
    Graphics.Refresh()
```
2. Drawing the Rectangle onto the display:
Let's start by inserting this line of code to draw the rectangle onto the display
`Graphics.drawRect(rect)`
Final code:
```
  from pybricks import *
  from LWPGE import *
  while True:
    rect = Rect(1,1,2,2,100)
    Graphics.drawRect(rect)
    Graphics.Clock(60)
    Graphics.Refresh()
```
You have a 2x2 square at 1,1 of the display at 100 brightness
### Congrats on finishing the tutorial
