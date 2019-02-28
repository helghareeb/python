# بسم الله ارحمن الرحيم

# Create Two Circles

# Method 01

from graphics import *

win = GraphWin()

left_circle = Circle(Point(80,50),5)
left_circle.setFill('yellow')
left_circle.setOutline('red')
left_circle.draw(win)

right_circle = Circle(Point(100,50), 5)
right_circle.setFill('yellow')
right_circle.setOutline('red')
right_circle.draw(win)

win.wait_window()