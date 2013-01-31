from GraphicsLibrary import *
import threading


# Still figuring out how to implement threads...
class Graphics():
    Window = GraphicsWindow('Empty', 100, 100)
    FillColor = Color.none
    mouseX, mouseY
    toLoop = False

    #Actually we probably should start thread in draw
    def setup(window_title, width, height):
        thread_draw = GraphicsWrapper()
        thread_draw.start()
        thread_draw.gSetup(window_title, width, height)


class GraphicsWrapper(threading.Thread):
    global Window

    def __init__(self, window):
        Thread.__init__()
        Window = window

    def run(self):
        global toLoop
        while (toLoop):
            draw()

    def canvas(window_title, width, height):
        Window = GraphicsWindow(window_title, width, height)

    def line((x1, y1), (x2, y2), color=None):
        global FillColor
        if color == None:
            color = FillColor
        new_line = Line(self, (x1, y1), (x2, y2))
        Window.draw(new_line)

    def rect((x, y), rectWidth, rectHeight, color=None, filled=True, stroke=False):
        global FillColor
        if color == None:
            color = FillColor
        new_rect = Rectangle(self, (x, y), rectWidth, rectHeight, color, true)
        Window.draw(new_rect)

    def circle((x, y), radius, color=None, filled=True, stroke=False):
        global FillColor
        if color == None:
            color = FillColor
        new_circle = Circle(self, (x, y), radius, FillColor, filled, stroke)
        Window.draw(new_circle)

    def ellipse((x, y), width, height, color=None, filled=True, stroke=False):
        global FillColor
        if color == None:
            color = FillColor
        new_ellipse = Ellipse(self, (x, y), width, height, color, filled)
        Window.draw(new_ellipse)

# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?
    def drawImage((x, y), imagePath, width, height):
        global Window
        img = Image((x, y), imagePath, width, height)
        Window.draw(img)

    def setBackground(r, g, b):
        global Window
        Window.contentPane.background = (r, g, b)

    def draw():
        for img in Window.objs:
            img._draw(Window)


#################################### Example #####################################

# Can create static sketches by not using setup or draw and putting code in "main"
drawLine((x1, y1), (x2, y2))
drawRect((x, y), rectWidth, rectHeight)
drawPolygon((x1, y1), (x2, y2), (x3, y3))
# What if have code in "main" and have setup and draw methods

setSize(300, 400)  # sets window size
setFrameRate(35)  # Can be set or not (default)
setStroke(red)  # Sets line drawing color to red
setStroke(125)  # Sets line drawing color to (125, 125, 125) (easy for white/grays/black)
setStroke(126, 35, 92)  # Sets line drawing color to (126, 35, 92)

noLoop()    # Causes draw to not be looped
loop()      # Causes draw to be looped (default?)
redraw()    # Calls draw once; useful for events


# Gets repeatedly called until program ends (window closes?)
def draw():
    setBackground(blue)

    # height and width are global variables and are from setSize()
    y = height
    x = width

    drawLine((x1, y1), (x2, y2))
    drawRect((x, y), rectwidth, rectheight)
    # etc.

    if (mousePressed):
        setStroke(255)
    else:
        setStroke(0)

    # Takes all the color definitions like setStroke
    setFill()
    # If drawFilledRect() is called with different stroke and fill colors,

    # mouseX and mouseY are the current mouse coordinates
    drawLine(mouseX - 66, mouseY, mouseX + 66, mouseY)
    drawLine(mouseX, mouseY - 66, mouseX, mouseY + 66)

    img = loadImage('path')
    drawImage(img, (x, y), imageWidth, imageHeight)
    drawImage(img, (x, y))  # Draws image at the original width and height


def mousePressed():
    # Perform some magic
    drawRect((x, y), mouseX, mouseY)

drawFunction(draw)
mousePressedFunction(mousePressed)
