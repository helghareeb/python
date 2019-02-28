# بسم الله الرحمن الرحيم

from graphics import *

# Create an empty window with default parameters
win = GraphWin()

# Create a new line at x,y
p0 = Point(50,60)
# Draw the line
p0.draw(win)

win.getMouse()

p1 = Point(140,100)
p1.draw(win)

# Just to prevent the window from closing before watching the output
win.wait_window()