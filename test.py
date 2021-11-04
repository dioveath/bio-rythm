from graphics import *
import math
import datetime


# Our window width and height (globals)
W_WIDTH = 1280                   # window with
W_HEIGHT = 720


# pixels per unit for our coordinate system
G_XUNIT = 18
G_YUNIT = 200

# resolution of graph
G_RES = 1

G_DRANGE = 30


G_ORIGINX = 0
G_ORIGINY = 0



# BIORYTHMS FORMULA
f_physical = lambda t : math.sin(math.pi * t / 23)
f_emotional = lambda t : math.sin(math.pi * t / 28)
f_intellectual = lambda t : math.sin(math.pi * t / 33)

# Plots grids as well as the current days
def PlotGrids(win, min_x, max_x, color, tdate):
    x = min_x

    todaydate = tdate
    deltatime_index = datetime.timedelta(days=-G_DRANGE)

    mid_x = int((min_x + max_x)/2)

    while(x <= max_x):
        tempLen = G_YUNIT


        spacing_p1 = Point(x * G_XUNIT + G_ORIGINX, W_HEIGHT/2 - tempLen)
        spacing_p2 = Point(x * G_XUNIT + G_ORIGINX, W_HEIGHT/2 + tempLen)
        line = Line(spacing_p1, spacing_p2)
        line.setFill(color)
        if(x == mid_x):
            line.setWidth(2)
        line.draw(win)


        tempdate = todaydate + deltatime_index

        dayText = Text(Point(x * G_XUNIT + G_ORIGINX, W_HEIGHT/2 + G_YUNIT + 20), str(tempdate.day))
        dayText.setSize(8)
        dayText.draw(win)

        deltatime_index += datetime.timedelta(days=1)
        
        x += G_RES

    offset = (W_HEIGHT - G_YUNIT * 2)/2
    y = offset
    percent = 100
    while(y <= (W_HEIGHT - offset)):
        spacing_p1 = Point(x * G_XUNIT + G_ORIGINX - G_XUNIT, y)
        spacing_p2 = Point(x * G_XUNIT + G_ORIGINX - (G_DRANGE * 2) * G_XUNIT - G_XUNIT, y)

        line = Line(spacing_p1, spacing_p2)
        line.setFill(color)
        line.draw(win)

        percentText = Text(Point(x * G_XUNIT + G_ORIGINX + 40, y), str(percent) + " % ")
        percentText.setSize(10)
        percentText.draw(win)

        percent -= 5

        y += (G_YUNIT/10)

        


# module to plot a function given f on win
# according to set of parameters from global
# virtual co-ordinate system within our window 
def PlotFunction(f, win, min_x, max_x, color):
    x = min_x
    prev_point = Point(x * G_XUNIT + G_ORIGINX, -f(x) * G_YUNIT + G_ORIGINY)

    while(x <= max_x):
        y = f(x)
        current_point = Point(x * G_XUNIT + G_ORIGINX , -y * G_YUNIT + G_ORIGINY)
        line = Line(prev_point, current_point)
        line.setFill(color)
        line.setWidth(2)
        line.draw(win)
        prev_point = current_point
        x += G_RES

        



# setup cartesian coordinate system based on origin x, y parameter
def SetupGraph(win, x, y):
    HAxis = Line(Point(0, y), Point(W_WIDTH, y)) 
    VAxis = Line(Point(x, 0), Point(x, W_HEIGHT))

    HAxis.draw(win)
    VAxis.draw(win)

    global G_ORIGINX
    global G_ORIGINY

    G_ORIGINX = x
    G_ORIGINY = y
    

# def PointInBounds(p, gObject):
    




def main():
    win = GraphWin("Test", W_WIDTH, W_HEIGHT)

    introText = Text(Point(W_WIDTH/2, W_HEIGHT/2 - 150), "Did you ever want to how much efficient you are certain days?")
    introText.setSize(24)
    introText.setTextColor("blue")
    introText2 = Text(Point(W_WIDTH/2, W_HEIGHT/2 - 100), "Fear not, We have what you need, Behold 'Biorythm'!")
    introText2.setSize(20)
    introText2.setTextColor("blue")
    questionText = Text(Point(W_WIDTH/2, W_HEIGHT/2 - 50), "Just Enter your Birth date (%d %M %Y): For e.g. 20 Jan 1990")
    disclaimerText = Text(Point(W_WIDTH/2, W_HEIGHT/2 - 25), "Disclaimer: Batteries not included! and No Garuantee!")
    disclaimerText.setSize(9)
    disclaimerText.setTextColor("red")
    dobText = Text(Point(W_WIDTH/2 - 100, W_HEIGHT/2), "Your DOB: ")
    targetText = Text(Point(W_WIDTH/2 - 100, W_HEIGHT/2 + 100), "Target Date: ")


    
    introText.draw(win)
    introText2.draw(win)
    disclaimerText.draw(win)
    questionText.draw(win)
    dobText.draw(win)
    dob= Entry(Point(W_WIDTH/2, W_HEIGHT/2), 10)
    dob.draw(win)
    targetText.draw(win)
    targetdate= Entry(Point(W_WIDTH/2, W_HEIGHT/2 + 100), 10)
    targetdate.draw(win)


    button = Text(Point(W_WIDTH/2, W_HEIGHT/2 + 200), " Click anywhere to Continue! ")
    button.setSize(20)
    button.draw(win)

    clickPoint = win.getMouse()

    dobText.undraw()
    targetText.undraw()
    dob.undraw()
    targetdate.undraw()
    button.undraw()
    questionText.undraw()
    introText.undraw()
    introText2.undraw()
    disclaimerText.undraw()

    dob_obj = datetime.datetime.strptime(dob.getText(), "%d %b %Y")
    tar_dateobj = datetime.datetime.strptime(targetdate.getText(), "%d %b %Y")

    rem_dateobj = tar_dateobj - dob_obj

    # print(dob_obj)
    # print(cur_dateobj)
    # print(rem_dateobj)

    md = rem_dateobj.days

    # global G_DRANGE
    # global G_XUNIT
    # global G_YUNIT
    # G_DRANGE = (int) (md/2)
    # print(G_DRANGE)
    # if(G_DRANGE > W_WIDTH):
    #     G_XUNIT = 1
    # else:
    #     G_XUNIT = W_WIDTH

    mdpx = md * G_XUNIT

    ox = -(mdpx - W_WIDTH/2) - G_DRANGE/2 
    oy = W_HEIGHT/2

    SetupGraph(win, ox, oy)


    PlotGrids(win, md - G_DRANGE, md + G_DRANGE, "gray", tar_dateobj)

    PlotFunction(f_physical, win, md - G_DRANGE, md + G_DRANGE, "red")
    PlotFunction(f_emotional, win, md - G_DRANGE, md + G_DRANGE, "green")
    PlotFunction(f_intellectual, win, md - G_DRANGE, md + G_DRANGE, "blue")



    title_text = Text(Point(W_WIDTH/2, 100), "BIORYTHM CHART")
    title_text.setSize(24)
    title_text.draw(win)

    circle_physical = Circle(Point(W_WIDTH - 300, W_HEIGHT - 100), 10)
    circle_physical.setFill("red")
    circle_physical.setOutline("red")
    circle_physical.draw(win)
    text_physical = Text(Point(W_WIDTH - 200, W_HEIGHT - 100), "Physical")
    text_physical.setSize(18)
    text_physical.setFill("red")
    text_physical.setFace("courier")
    text_physical.draw(win)

    circle_emotional = Circle(Point(W_WIDTH - 300, W_HEIGHT - 70), 10)
    circle_emotional.setFill("green")
    circle_emotional.setOutline("green")
    circle_emotional.draw(win)
    text_emotional = Text(Point(W_WIDTH - 200, W_HEIGHT - 70), "Emotional")
    text_emotional.setSize(18)
    text_emotional.setFace("courier")
    text_emotional.setFill("green")
    text_emotional.draw(win)

    circle_intellectual = Circle(Point(W_WIDTH - 300, W_HEIGHT - 40), 10)
    circle_intellectual.setFill("blue")
    circle_intellectual.setOutline("blue")
    circle_intellectual.draw(win)
    text_intellectual = Text(Point(W_WIDTH - 200, W_HEIGHT - 40), "Intellectual")
    text_intellectual.setSize(18)
    text_intellectual.setFace("courier")
    text_intellectual.setFill("blue")
    text_intellectual.draw(win)



    win.getMouse()
    win.close()



main()



    




    
