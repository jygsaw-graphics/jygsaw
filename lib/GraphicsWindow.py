from java.awt.event import ActionListener, KeyListener, MouseListener
from java.awt.Color import * # so we can just say gray instead of Color.gray
from javax.swing import JFrame, JPanel
from javax.swing.event import MouseInputListener
from java.lang import Math
from Image import *
from Group import *
from Shape import *
from Text import *


# Buttons, etc
# class Components:


class GraphicsWindow(ActionListener, KeyListener, MouseInputListener):
    #we need motion input using MouseInputListener
    def __init__(self, title, width, height, backgroundColor = white):
        assert width > 0, "GraphicsWindow width must be greater than zero"
        assert height > 0, "GraphicsWindow height must be greater than zero"
        self.objs = [] # List of Jy_Objects
        self.width = width
        self.height = height
        self.frame = JFrame(title,defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
                            size = (self.width, self.height))
        self.frame.contentPane = Canvas(self, self.objs, backgroundColor)
        self.frame.addMouseListener(self) 
        self.frame.addMouseMotionListener(self)
        self.frame.addKeyListener(self)
        self.mouseX = 0
        self.mouseY = 0
        
        #MouseEvent booleans mousePressed, mouseClicked, mouseDragged
        self.mouseP = False
        self.mouseC = False
        self.mouseD = False
    
        #KeyEvent booleans keyPressed, keyTyped
        self.keyP = False
        self.keyT = False
    
    def setVisible(self, isVisible):
        self.frame.visible = isVisible
    
    # this argument takes a variable length number of GraphicsObjects and Group objects
    # using the splat operator, which packages the args into a tuple.
    # We iterate through each element in the tuple,
    # and add it to our self.objs.
    def draw(self, *params):        
        for arg in params:
            if isinstance(arg, GraphicsObject):
                self.objs.append(arg)
            elif isinstance(arg, Group):
                for obj in arg.group:
                    self.objs.append(obj)
            else:
                print "you passed in something that's not a group or graphics object"

    def setDefaultColor(self, c):
        self.frame.contentPane.setDefaultColor(c)

    #We put these mouse location methods in the window class in case we implement multiple panels    
    #MouseListener methods
    def mouseEntered (self, e):
        self.mouseX = e.getXOnScreen()
        self.mouseY = e.getYOnScreen()
        print self.mouseX
        print self.mouseY
    def mouseX (self):
        return self.mouseX    
    def mouseY (self):
        return self.mouseY
    def mouseClicked (self,e):
        self.mouseC = True
    def mouseExited (self,e):
        pass
    def mousePressed (self,e):
        self.mouseP = True
    def mouseReleased (self,e):
        self.mouseP = False
        self.mouseC = False
        self.mouseD = False
    def mouseMoved (self,e):
        self.mouseX = e.getXOnScreen()
        self.mouseY = e.getYOnScreen()
        print self.mouseX
        print self.mouseY
    def mouseDragged (self,e):
        self.mouseD = True
        
    #KeyListener methods
    def keyTyped (self,e):
        self.keyT = True
        print e.getKeyChar()
    def keyPressed (self,e):
        self.keyP = True
        print e.getKeyChar()
    def keyReleased (self,e):
        self.keyT = False
        self.keyP = False

class Canvas(JPanel):
    """ Canvas to draw the action on. Owns the action and key listeners. """
    
    def __init__(self, window, objects, backgroundColor):
        self.objs = objects
        self.window = window
        self.defaultColor = gray
        self.backgroundColor = backgroundColor
    
    def paintComponent(self, g):
        g.background = self.backgroundColor
        g.clearRect(0, 0, self.window.width, self.window.height)
        g.setColor(white) # Set color of rectangle
        
        print 'Canvas # objs', len(self.objs)
        
        for i in range(len(self.objs)):
            if self.objs[i].color == None:
                g.setColor(self.defaultColor)
            else:
                g.setColor(self.objs[i].getColor())
            self.objs[i]._draw(g)

    def setDefaultColor(self, c):
        self.defaultColor = c


