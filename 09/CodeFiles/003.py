# بسم الله ارحمن الرحيم

# Create Two Circles

# Method 02

from graphics import *

win = GraphWin()

left_circle = Circle(Point(80,50),5)
left_circle.setFill('yellow')
left_circle.setOutline('red')

right_circle = left_circle.clone()

left_circle.draw(win)
right_circle.move(20, 0)
right_circle.draw(win)

win.wait_window()