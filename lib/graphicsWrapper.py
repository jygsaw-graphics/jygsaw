from GraphicsObject import *
from GraphicsWindow import *
from Group import *
from Image import *
from Shape import *
from Text import *
from java.awt.Color import *
import time


toLoop = False
Stroke = False
fR = 48 # Frame Rate

"""
Creates a new window. Width, height and title can be set optionally as well
"""


def canvas(width=400, height=400, window_title=' ', background=white):
    global window
    window = GraphicsWindow(window_title, width, height, background)
    window.setVisible(True)

"""
Returns the width of the window
"""


def width():
    return window.w

"""
Returns the width of the window
"""


def height():
    return window.h

"""
Draws a line between coordinates (x1, y1), and (x2 and y2). You can optionally set the color as well
"""


def line(x1, y1, x2, y2, color=None):
    new_line = Line((x1, y1), (x2, y2))
    window.draw(new_line)
    return new_line

"""
Creates a rectangle with the upper left corner at the given (x,y) coordinates.
"""


def rect(x, y, rectWidth=100, rectHeight=100, color=None, filled=True, stroke=Stroke):
    new_rect = Rectangle((x, y), rectWidth, rectHeight, color, filled)
    window.draw(new_rect)
    return new_rect

"""
Creates a circle centered at the given (x,y) coordinates. The radius, color, filled status, and stoke status can be
optionally modified.
"""


def circle(x, y, radius=50, color=None, filled=True, stroke=Stroke):
    new_circle = Circle((x, y), radius, color, filled)
    window.draw(new_circle)
    return new_circle

"""
Creates an eclipse centered at the given (x,y) coordinates. Width, height, color, filled status and stroke status
can be optionally modified.
"""


def ellipse(x, y, width=100, height=100, color=None, filled=True, stroke=Stroke):
    new_ellipse = Ellipse((x, y), width, height, color, filled)
    window.draw(new_ellipse)
    return new_ellipse

"""
Creates a polygon whose points are given in a list as the first argument. Width, height, color, filled status and stroke status can
be optionally modified
"""


def polygon(vertices, color=None, filled=True, stroke=Stroke):
    new_polygon = Polygon(vertices, color, filled)
    window.draw(new_polygon)
    return new_polygon

"""
Creates an arc centered at the given (x,y) coordinates. The width, heigh, start angle, end angle, color, filled
status and stoke status can be optionally modified. Start angle and end angle refer to the
"""


def arc(x, y, width=100, height=100, startAngle=0, endAngle=180, color=None, filled=True, stroke=Stroke):
    new_arc = Arc(
        (x, y), width, height, startAngle, (endAngle - startAngle), color)
    window.draw(new_arc)
    return new_arc

# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?

"""
Draws an image with upper left corner at the given (x,y) coordinates. The image should be located at imagePath,
and the desired width and height of the image should be specified in their respective arguments.
"""


def image(x, y, imagePath, width, height):
    global window
    img = Image((x, y), imagePath, width, height)
    window.draw(img)
    return img

"""
Sets the color to fill shapes with.
"""


def fill(color):
    window.setDefaultColor(color)

"""
Sets the background color of the window.
"""


def setBackground(color):
    window.setBackgroundColor(color)
    # It would be nice to be able to accept multiple types of color input
    # (r,g,b or name of color)



#-----------Mouse and Key Listener functions---------------
"""
Returns x coordinate of the mouse
"""
def mouseX():
    return window.mouseX

"""
Returns y coordinate of the mouse
"""
def mouseY():
    return window.mouseY

"""
Sets the window's onMousePressed variable to be the user defined mouseClicked function.
It will then be called by the window's mouse listener when the event occurs.
"""
def onMousePress(mousePressed):
    window.onMousePressed = mousePressed

"""
Sets the window's onMouseReleased variable to be the user defined mouseClicked function.
It will then be called by the window's mouse listener when the event occurs.
"""
def onMouseRelease(mouseReleased):
    window.onMouseReleased = mouseReleased

"""
Sets the window's onMouseClick variable to be the user defined mouseClicked function.
It will then be called by the window's mouse listener when the event occurs.
"""
def onMouseClick(mouseClicked):
    window.onMouseClick = mouseClicked

"""
Sets the window's onMouseDragged variable to be the user defined mouseDragged function.
It will then be called by the window's mouse listener when the event occurs.
"""
def onMouseDrag(mouseDragged):
    window.onMouseDragged = mouseDragged

"""
Sets the window's onMouseMoved variable to be the user defined mouseMoved function.
It will then be called by the window's mouse listener when the event occurs.
"""
def onMouseMove(mouseMoved):
    window.onMouseMoved = mouseMoved

#---------------------------------------------------------------
    
"""
Sets stroke to false
"""
def noStroke():
    global Stroke
    Stroke = False

"""
Tells the draw function to loop when it is called
"""
def loop():
    global toLoop
    toLoop = True

"""
Tells the draw function not to loop when it is called,
or to stop looping if it has already started. This is the default.
"""
def noLoop():
    global toLoop
    toLoop = False


"""
Sets the frame rate value
"""
def frameRate(rate):
    global frameRate
    frameRate = rate

"""
Sets stroke to true
"""
def stroke():
    global Stroke
    Stroke = True


"""
Clears the window of all objects
"""
def clear():
    window.clear()

"""
Callback function which calls the user defined draw function.
It repeatedly loops if loop() has been called.
"""
def onDraw(draw):
    if toLoop:
        while toLoop:
            draw()
            time.sleep(1/fR)
    else:
        draw()

"""
Redraws all of the objects on the window. Not sure there is a point to it.
"""


def redraw():
    window.redraw()

if ( __name__ == '__main__' ) or ( __name__ == 'main' ):
    canvas()
    loop()
    frameRate(48)

    x = None
    y = None

    rectX = 10
    rectY = 10

    def draw():
        global rectX
        global rectY
        clear()
        vertices = [(250,250),(360,360), (360, 250)]
        
        fill(red)
        rect(rectX,rectY)
        line(150, 10, 200, 10)
        fill(pink)
        ellipse(10, 150)
        
        print width(), height()
        
        polygon(vertices)
        arc(300, 100)
        #circle(10,110)
        
        setBackground(black)
        rectX = rectX + 10
        rectY = rectY + 10

    def mousePressed():
        print 'Mouse was pressed.'

    def mouseDragged():
        print 'Mouse is being dragged.'
        print 'X = ' + str(x) + ' Y = ' + str(y)

    def mouseReleased():
        print 'Mouse released'

    def mouseClicked():
        print 'Mouse clicked'

    def mouseMoved():
        global x, y
        x = mouseX()
        y = mouseY()
        print 'Mouse moved x = %d, y = %d' % (x, y)

    onMousePress(mousePressed)
    onMouseRelease(mouseReleased)
    onMouseDrag(mouseDragged)
    onMouseMove(mouseMoved)
    onMouseClick(mouseClicked)
    onDraw(draw)

    

