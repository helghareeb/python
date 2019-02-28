# بسم الله الرحمن الرحيم

# Visual Representation of Data

from graphics import *

# Create a 320x240 GraphWin titled ''Investment Growth Chart''
win = GraphWin(title='Investment Growth Chart', width=320, height=240)

# Draw label ' O . OK' at (20 , 230)
Text(Point(20,230),' 0.0K').draw(win)

# Draw label ' 2 . 5K' at (20 , 180)
Text(Point(20, 180), ' 2.5K').draw(win)

# Draw label ' 5 . 0K' at (20 , 130)
Text(Point(20, 130), ' 5.0K').draw(win)

# Draw label ' 7 . 5K' at (20 , 80)
Text(Point(20, 80), ' 7.5K').draw(win)

# Draw label '10 . 0K' at (20 , 30)
Text(Point(20, 30), '10.0K').draw(win)

# Draw a rectangle from (40, 230) to (65 , 230 - principal * 0.02)

principal = 2000
apr = .12

# Draw bar for initial principal
height = principal * 0.02
bar = Rectangle(Point(40, 230), Point(65, 230-height))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

# Draw bars for successive years
for year in range(1,11):
    # calculate value for the next year
    principal = principal * (1 + apr)
    # draw bar for this value
    xll = year * 25 + 40
    height = principal * 0.02
    bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


win.wait_window()