# typewriter.py
#
# Jygsaw demo - Implements a typewriter with Jygsaw
#
# Attribution: inspired by the words demo in Processing
# from http://processingjs.org/learning/basic/words/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *

canvas(750, 360)
background(darkGray)
currentLineHeight = 60
textHeight = 30
words = ""
textList = []


def draw():
    global currentLineHeight, textHeight, words
    clear()

    t = text(25, 25, "Type onto the screen:", color=gray, attribute=PLAIN)
    t._set_size(textHeight)
    t._set_font("Georgia")

    for (i, h) in textList:
        ti = text(25, h, i, color=white, attribute=PLAIN)
        ti._set_font("Arial")
        ti._set_size(textHeight)

    tw = text(25, currentLineHeight, words, color=white, attribute=PLAIN)
    tw._set_font("Arial")
    tw._set_size(textHeight)


def keyPressed():
    global words, textList, currentLineHeight, textHeight
    k = lastKeyChar()
    c = lastKeyCode()
    if (c != 10 and c != 16):  # as long as the key pressed is not a return or shift
        words += k
    elif c == 10:  # else if the key pressed is a return
        newLine = words
        words = ""
        textList.append((newLine, currentLineHeight))
        currentLineHeight += textHeight  # lower the current line by textHeight

onKeyPress(keyPressed)
onDraw(draw)

jygsawMain(0.01)
