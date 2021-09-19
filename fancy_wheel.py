# hw6.py
# name + andrewId + section

#Place the Autograded solutions here




######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#Place the manually graded solutions here

from tkinter import *
import math

####################################
# FancyWheels
####################################

def fancyWheelsInit(data):
    # load data.xyz as appropriate
    data.dimension = 5   # 5x5

    data.shape_side = 4  # start with 4 side
    
    data.space = data.width / data.dimension
    
    data.radius = data.space / 2.2
    
    data.color_increment = 255 / (data.dimension - 1)

    data.start_angle_even = 0
    data.start_angle_odd = 0


def fancyWheelsMousePressed(event, data):
    # use event.x and event.y
    pass

def fancyWheelsKeyPressed(event, data):
    # use event.char and event.keysym
    if(event.keysym == 'Left'):
        data.dimension -= 1
        data.space = data.width / data.dimension
        data.radius = data.space / 2
        data.color_increment = 255 / (data.dimension - 1)
    
    elif(event.keysym == 'Right'):
        data.dimension += 1
        data.space = data.width / data.dimension
        data.radius = data.space / 2
        data.color_increment = 255 / (data.dimension - 1)

def fancyWheelsTimerFired(data):
    data.start_angle_even += math.radians(10)
    data.start_angle_odd -= math.radians(10)


def fancyWheelsRedrawAll(canvas, data):
    for i in range(data.dimension):
        for j in range(data.dimension):
            drawshape(data,canvas, data.radius + j*data.space,data.radius+i*data.space,data.radius, data.shape_side+i+j, i ,j)

    


def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawshape(data,canvas, centerX, centerY, radius, side, col, row):
    coordinatesX = []
    coordinatesY = []
    for i in range(side):
        angle =  i*2*math.pi/side
        
        if(side % 2 == 0):
            X = centerX + radius * math.cos(data.start_angle_even + angle)
            coordinatesX.append(X)
            Y = centerY + radius * math.sin(data.start_angle_even + angle)
            coordinatesY.append(Y)
        elif(side % 2 == 1):
            X = centerX + radius * math.cos(data.start_angle_odd + angle)
            coordinatesX.append(X)
            Y = centerY + radius * math.sin(data.start_angle_odd + angle)
            coordinatesY.append(Y)


    for i in range(side):
        for j in range(i,side):
            if(i == j):
                pass
            else:
                canvas.create_line(coordinatesX[i],coordinatesY[i],coordinatesX[j],coordinatesY[j],
                fill = rgbString(int(0 + col*data.color_increment),int(255 - row*data.color_increment),0))

####################################
# run function for FancyWheels
####################################

def runFancyWheels(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        fancyWheelsRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        fancyWheelsMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        fancyWheelsKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        fancyWheelsTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    fancyWheelsInit(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

runFancyWheels(600,600)
