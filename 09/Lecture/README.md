# بسم الله الرحمن الرحيم

[TOC]

# Primitive Graphics in OOP

## Point

- 000.py

## Basic Shapes
The library provides the following graphical objects:
- Point
- Line
- Circle
- Oval
- Rectangle
- Polygon
- Text
- Entry (for text-based input)
- Image

- 001.py

## Two Circles - Primitive Method

- 002.py

## Two Circles - Clone

- 003.py

## Visual Representation of Data

- 004.py

## Graphics Objects
Generally, Graphics Objects needs to satisfy the following requirements
- ```setFill (color)``` Sets the interior of the object to the given color. 
  ```
  someObject . setFill ( "red" )
  ```
- ```setOutline (color)``` Sets the outline of the object to the given color. 
  ```
  someObject . setOutline ( "yellow" )
  ```
- ```setWidth (pixels)``` Sets the width of the outline of the object to the desired number of pixels. (Does not work for Point.) 
  ```
  some0bject . setWidth (3)
  ```
- ```draw (aGraphWin)``` Draws the object into the given GraphWin and returns the drawn object. 
  ```
  someObject . draw (someGraphWin)
  ```
- ```undraw()``` Undraws the object from a graphics window. If the object is not currently drawn, no action is taken. 
  ```
  someObject . undraw ()
  ```
- ```move (dx , dy)``` Moves the object dx units in the x direction and dy units in the y direction. If the object is currently drawn, the image is adjusted to the new position. 
  ```
  some0bject . move ( 10 , 15 . 5)
  ```
- ```clone ()``` Returns a duplicate of the object. Clones are always created in an undrawn state. Other than that, they are identical to the cloned object. 
  ```python
  objectCopy = someObject.clone ()
  ```

### Point Methods
- ```Point (x , y)``` Constructs a point having the given coordinates.
  ```
  aPoint = Point (3 . 5 , 8)
  ```

- ```getX ()``` Returns the x coordinate of a point.
  ```
  xValue = aPoint . getX()
  ```

- ```getY ()``` Returns they coordinate of a point.
  ```
  yValue = aPoint . getY ()
  ```

### Line Methods
- ```Line (point! , point2)``` Constructs a line segment from point! to point2.
  ```
  aLine = Line (Point ( 1 , 3) , Point (7 , 4) )
  ```
- ```setArrow ( endString)``` Sets the arrowhead status of a line. Arrows may be drawn at either the first point, the last point, or both. Possible values of endString are "first ", " last " , "both" , and "none " . The default setting is "none " .
  ```
  aLine . setArrow ( "both" )
  ```
  - ```getCenter ()``` Returns a clone of the midpoint of the line segment.
  ```
  midPoint = aLine . getCenter ()
  ```
  - ```getP1 () , getP2 ()``` Returns a clone of the corresponding endpoint of the segment.
  ```
  startPoint = aLine . getP1 ( )
  ```

### Circle Methods
- ```Circle (centerPoint , radius)``` Constructs a circle with the given center point and radius.
  ```
  aCircle = Circle (Point (3 , 4) , 10 . 5)
  ```
- ```getCenter()``` Returns a clone of the center point of the circle.
  ```
  centerPoint = aCircle . getCenter ( )
  ```
- ```getRadius ()``` Returns the radius of the circle.
  ```
  radius = aCircle . getRadius ( )
  ```
- ```getP1 ()``` , ```getP2 ()``` Returns a clone of the corresponding corner of the circle's bounding box. These are opposite corner points of a square that circumscribes the circle.
  ```
  cornerPoint = aCircle . getP1 ()
  ```

### Rectangle Methods
- ```Rectangle (point 1 , point2)``` Constructs a rectangle having opposite corners at point 1 and point2.
  ```
  aRectangle = Rectangle (Point ( 1 , 3) , Point (4 , 7) )
  ```
- ```getCenter ()``` Returns a clone of the center point of the rectangle.
  ```
  centerPoint = aRectangle . getCenter ()
  ```
- ```getP1 ()``` , ```getP2 ()``` Returns a clone of the corresponding point used to construct the rectangle.
  ```
  cornerPoint = aRectangle . getP1 ( )
  ```

### Oval Methods
- ```Oval (point 1 , point2)``` Constructs an oval in the bounding box determined by point 1 and point2.
  ```
  anOval = Oval (Point ( 1 , 2) , Point (3 , 4) )
  ```
- ```getCenter ()``` Returns a clone of the point at the center of the oval.
  ```
  centerPoint = anOval . getCenter ( )
  ```
- ```getP1 ()``` , ```getP2 ()``` Returns a clone of the corresponding point used to construct the oval.
  ```
  cornerPoint = an0val . getP1 ()
  ```
### Polygon Methods
- ```Polygon (point 1 , point2 , point3 , . . . )``` Constructs a polygon with the given points as vertices. Also accepts a single parameter that is a list of the vertices.
  ```
  aPolygon = Polygon (Point ( 1 , 2) , Point (3 , 4) , Point (5 , 6) )
  aPolygon = Polygon ( [Point ( 1 , 2) , Point (3 , 4) , Point (5 , 6) ] )
  ```
- ```getPoints ()``` Returns a list containing clones of the points used to construct the polygon.
  ```
  pointList = aPolygon . getPoints ( )
  ```

### Text Methods
- ```Text (anchorPoint , textString)``` Constructs a text object that displays textString centered at anchorPoint. The text is displayed horizontally.
  ```
  message = Text (Point (3 , 4) , "Hello ! " )
  ```
- ```setText (string)``` Sets the text of the object to string.
  ```
  message . setText ( "Goodbye ! " )
  ```
- ```get Text ( )``` Returns the current string.
  ```
  msgString = message . getText ()
  ```
- ```getAnchor ()``` Returns a clone of the anchor point.
  ```
  centerPoint = message . getAnchor ( )
  ```
- ```setFace (family)``` Changes the font face to the given family. Possible values are "helvetica" , " courier", "times roman", and " arial " .
  ```
  message . setFace ( " arial " )
  ```
- ```setSize (point)``` Changes the font size to the given point size. Sizes from 5 to 36 points are legal.
  ```
  message . setSize ( 18)
  ```
- ```setStyle (style)``` Changes font to the given style. Possible values are: "normal " , "bold", " italic ", and "bold italic " .
  ```
  message . setStyle ( "bold" )
  ```
-```setTextColor``` (color) Sets the color of the text to color. Note: setFill has the same effect.
  ```
  message . setTextColor ( "pink" )
  ```

## Entry Objects
Objects of type Entry are displayed as text entry boxes that can be edited by
the user of the program. Entry objects support the generic graphics methods move () , draw(graphwin) , undraw () , setFill (color) , and clone () . The
Entry specific methods are given below.
- ```Entry (centerPoint , width)``` Constructs an Entry having the given center point and width. The width is specified in number of characters of text that can be displayed.
  ```
  inputBox = Entry (Point (3 , 4) , 5)
  ```
- ```getAnchor ()``` Returns a clone of the point where the entry box is centered.
  ```
  centerPoint = inputBox . getAnchor ()
  ```
- ```get Text ( )``` Returns the string of text that is currently in the entry box.
  ```
  inputStr = inputBox . getText ()
  ```
- ```setText (string)``` Sets the text in the entry box to the given string.
  ```
  inputBox . setText ( " 32 . 0 " )
  ```
- ```setFace (family)``` Changes the font face to the given family. Possible values are "helvetica" , " courier", "times roman", and " arial " .
  ```
  inputBox . setFace ( " courier " )
  ```
- ```setSize (point)``` Changes the font size to the given point size. Sizes from 5 to 36 points are legal.
  ```
  inputBox . setSize ( 12)
  ```
- ```setStyle (style)``` Changes font to the given style. Possible values are: "normal " , "bold", " italic " , and "bold italic " .
  ```
  inputBox . setStyle ( " italic " )
  ```
- ```setTextColor (color)``` Sets the color of the text to color.
  ```
  inputBox . setTextColor ( "green" )
  ```
## Displaying Images
The graphics module also provides minimal support for displaying and manipulating images in a GraphWin. Most platforms will support at least PPM and GIF images. Display is done with an Image object. Images support the generic methods ```move (dx , dy)``` , ```draw(graphwin)``` , ```undraw ()``` , and ```clone ( )``` . Image-specific methods are given below.
- ```Image (anchorPoint , f ilename)``` Constructs an image from contents of the given file, centered at the given anchor point. Can also be called with width and height parameters instead of f ilename. In this case, a blank (transparent) image is created of the given width and height (in pixels).
  ```
  flowerimage = Image (Point ( 100 , 100) , "flower . gif " )
  ```
  ```
  blankimage = Image (320 , 240)
  ```
- ```getAnchor()``` Returns a clone of the point where the image is centered.
  ```
  centerPoint = flowerimage . getAnchor ( )
  ```
- ```getWidth ()``` Returns the width of the image.
  ```
  widthinPixels = flowerimage . getWidth ( )
  ```
- ```getHeight ()``` Returns the height of the image.
  ```
  heightinPixels = flowerimage . getHeight ()
  ```
- ```getPixel (x , y)``` Returns a list [red , green , blue] of the RGB values of the pixel at position (x , y) . Each value is a number in the range 0-255 indicating the intensity of the corresponding RGB color. These numbers can be
turned into a color string using the color_rgb function (see next section).
Note that pixel position is relative to the image itself, not the window
where the image may be drawn. The upper-left comer of the image is
always pixel ( 0 , 0).
  ```
  red , green , blue = flowerimage . getPixel (32 , 18)
  ```
- ```setPixel (x , y , color)``` Sets the pixel at position (x , y) to the given color. Note: This is a slow operation.
  ```
  flowerimage . setPixel (32 , 18 , "blue " )
  ```
- ```save (filename)``` Saves the image to a file. The type of the resulting file (e.g.,GIF or PPM) is determined by the extension on the filename.
  ```
  flowerImage . save ( "mypic . ppm" )
  ```

## Generating Colors
- Colors are indicated by strings. Most normal colors such as "red", "purple ", "green", " cyan", etc. should be available.
- Many colors come in various shades, such as "red1 " ' "red2 " ' "red3 " ' "red4" ' which are increasingly darker shades of red. 
- The graphics module also provides a function for mixing your own colors numerically. 
- The function ```color_rgb (red , green , blue)``` will return a string representing a color that is a mixture of the intensities of red, green and blue specified. 
- These should be ints in the range 0-255. Thus ```color_rgb (255 , 0 , 0)``` is a bright red, while ```color_rgb ( 130 , 0 , 130)``` is a medium magenta.

```
aCircle . setFill (color_rgb ( 130 , 0 , 130) )
```

## Controlling Display Updates (Advanced)
- Usually, the visual display of a GraphWin is updated whenever any graphics object's visible state is changed in some way. 
- However, under some circumstances, for example when using the graphics library inside some interactive shells, it may be necessary to force the window to update in order for changes to be seen.
- The ```update ()``` function is provided to do this.
- ```update ()``` Causes any pending graphics operations to be carried out and the results displayed.
- For efficiency reasons, it is sometimes desirable to tum off the automatic updating of a window every time one of the objects changes. 
- For example, in an animation, you might want to change the appearance of multiple objects before showing the next "frame" of the animation. 
- The GraphWin constructor includes a special extra parameter called autoflush that controls this automatic
  updating. 
- By default, autoflush is on when a window is created. 
- To turn it off, the autoflush parameter should be set to False, like this:
```python
win = GraphWin ( "My Animation" , 400 , 400 , autoflush=False)
```
- Now changes to the objects in win will only be shown when the graphics system has some idle time or when the changes are forced by a call to update () .
- The update ( ) method also takes an optional parameter that specifies the maximum rate (per second) at which updates can happen. 
- This is useful for controlling the speed of animations in a hardware-independent fashion. 
- For example, placing the command update (30) at the bottom of a loop ensures