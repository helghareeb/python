# بسم الله الرحمن الرحيم

from graphics import *

# Create an empty window with default parameters
win = GraphWin(title='Image Demo',width=500,height=500)

# Add some Text
#txt = Text(Point(10,10),'Graphics Demo using graphics.py - By: Dr.Haitham El-Ghareeb')
#txt.draw(win)

# Load an Image
image = Image (Point ( 100 , 100) , "Lecture-03\CodeFiles\pacman.gif" )
image.draw(win)

win.getMouse()

image.move(50, 50)

# Just to prevent the window from closing before watching the output
win.wait_window()