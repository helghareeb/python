# بسم الله الرحمن الرحيم

from graphics import *

win = GraphWin(title='Basic Shapes', width=500, height=500)

# Draw a red circle, center point at (250,250)
center_point = Point(250,250)
my_circle = Circle(center_point, 100)
my_circle.setOutline('red')
my_circle.draw(win)

# Add textual label to the center of the circle
my_label = Text(center_point, 'Computer Graphics Course')
my_label.draw(win)

# Draw a square using a rectangle object
my_square = Rectangle(Point(30,30), Point(70,70))
my_square.draw(win)

# Draw line segment using Line object
my_line = Line(Point(20,30), Point(180,165))
my_line.draw(win)

# Draw an oval using an obal object
my_oval = Oval(Point(20,150), Point(180, 199))
my_oval.draw(win)

win.wait_window()