class knots:
    stringdictionary = {}
    stringsdefined = 0
    turtledictionary = {}
    turtlesdefined = 0
    stringnumber = 0
    turtleonstring = {}
    turtledictionary = {}

    def __init__(self, strings, stringinput, distance, dotsize = 10, velocity = 2):
        stringinput = input("1: Red\n2:Orange\n3:Yellow\n4:Green\n5:Blue\n6:Purple\n7:Black\nInput string pattern ("+ str(strings)+ " strings):")
        import turtle
        import math
        turtle.setworldcoordinates(-50, -200, 200, 50)
        knots.hypdist = math.sqrt(2*(distance**2))
        knots.columndict = {}
        knots.distance = distance
        knots.dotsize = dotsize
        turtlesdefined = 0
        timesrun = 0
        rainbowlist = ["red", "orange", "gold", "green", "blue", "purple", "black"]
        colorlist = []
        if len(stringinput) > 0:
            for char in stringinput:
                stringcolor = rainbowlist[int(char)-1]
                colorlist.append(stringcolor)
        else:
            colorlist = rainbowlist
            colorsappended = 0
            while len(colorlist) < strings:
                colorlist.append(rainbowlist[colorsappended])
                #this will cause problems once we get beyond idk 16 strings
        for number in range(strings):
            knots.turtledictionary[str(number)] = turtle.Turtle()
        for eachturtle in knots.turtledictionary:
            turtlename = knots.turtledictionary[eachturtle]
            turtlename.color(colorlist[turtlesdefined])
            turtlename.speed(velocity)
            positiondistance = turtlesdefined*distance
            turtlename.forward(positiondistance) 
            turtlename.right(45)
            turtlename.rightfacing = True
            knots.columndict[turtlename] = turtlesdefined
            turtlesdefined += 1 
        row = 0
    
    def crossright(self, stringnumber):
        sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        #Provides a list of turtlevalues in order of string value (or should)
        leftturtle, rightturtle = sortcolumns[stringnumber], sortcolumns[stringnumber+1]
        if leftturtle.rightfacing == False:
            leftturtle.left(90)
            leftturtle.rightfacing = True
        if rightturtle.rightfacing == True:
            rightturtle.right(90)
            rightturtle.rightfacing = False
        leftturtle.forward(knots.hypdist/2)
        rightturtle.forward(knots.hypdist)
        leftturtle.dot(knots.dotsize)
        leftturtle.forward(knots.hypdist/2)
        knots.columndict[rightturtle] -= 1
        knots.columndict[leftturtle] += 1
     

    def crossleft(self, stringnumber):
        sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        #Provides a list of turtlevalues in order of string value (or should)
        leftturtle, rightturtle = sortcolumns[stringnumber], sortcolumns[stringnumber+1]
        if leftturtle.rightfacing == False:
            leftturtle.left(90)
            leftturtle.rightfacing = True
        if rightturtle.rightfacing == True:
            rightturtle.right(90)
            rightturtle.rightfacing = False
        rightturtle.forward(knots.hypdist/2)
        leftturtle.forward(knots.hypdist)
        rightturtle.dot(knots.dotsize)
        rightturtle.forward(knots.hypdist/2)
        knots.columndict[rightturtle] -= 1
        knots.columndict[leftturtle] += 1

    def turnright(self, stringnumber):
        sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        leftturtle, rightturtle = sortcolumns[stringnumber], sortcolumns[stringnumber+1]
        if leftturtle.rightfacing == False:
            leftturtle.left(90)
            leftturtle.rightfacing = True
        if rightturtle.rightfacing == True:
            rightturtle.right(90)
            rightturtle.rightfacing = False
        leftturtle.forward(knots.hypdist/2)
        rightturtle.forward(knots.hypdist/2)
        rightturtle.dot(knots.dotsize)
        rightturtle.left(90)
        rightturtle.rightfacing = True
        rightturtle.forward(knots.hypdist/2)
        leftturtle.right(90)
        leftturtle.rightfacing = False
        leftturtle.forward(knots.hypdist/2)
        
    def turnleft(self, stringnumber):
        sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        leftturtle, rightturtle = sortcolumns[stringnumber], sortcolumns[stringnumber+1]
        if leftturtle.rightfacing == False:
            leftturtle.left(90)
            leftturtle.rightfacing = True
        if rightturtle.rightfacing == True:
            rightturtle.right(90)
            rightturtle.rightfacing = False
        leftturtle.forward(knots.hypdist/2)
        rightturtle.forward(knots.hypdist/2)
        leftturtle.dot(knots.dotsize)
        rightturtle.left(90)
        rightturtle.rightfacing = True
        rightturtle.forward(knots.hypdist/2)
        leftturtle.right(90)
        leftturtle.rightfacing = False
        leftturtle.forward(knots.hypdist/2)
    def edge(self, stringnumber):
        sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        turtlename = sortcolumns[stringnumber]
        if turtlename.rightfacing == False:
            turtlename.left(45)
            turtlename.forward(knots.distance)
            turtlename.right(45)
        else:
            turtlename.right(45)
            turtlename.forward(knots.distance)
            turtlename.left(45)
    def stamp(self, stringnumber):
        sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        turtlename = sortcolumns[stringnumber]
        turtlename.stamp()

def diagAltStripes(strings = 6):  
    bracelet = knots(strings, stringinput = "", distance = 10)
    loops = 0
    while loops < 10:
        if loops%2 == 0:
            for x in range(strings-1):
                if x%2 == 0:
                    bracelet.crossright(x)
            for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
            for x in range(strings-1):
                if x%2 == 1:
                    bracelet.turnleft(x)
        else:   
            for x in range(strings-1):
                if x%2 == 0:
                    bracelet.turnleft(x)
            for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
            for x in range(strings-1):
                if x%2 == 1:
                    bracelet.turnleft(x)
        loops += 1
def diamond1(strings = 6, distance = 10, velocity = 2):
    bracelet = knots(strings, distance, velocity)
    loops = 0
    while loops < 10:
        for x in range(strings):
            if x%2 == 0:
                if x == strings or x == strings-2:
                    # bracelet.stamp(x)
                    bracelet.crossleft(x)
                else:
                    # print(x)
                    bracelet.crossright(x)
        for x in range(strings-1):
            if x%2 != 0:
                if x <= (strings-1)/2:
                    bracelet.crossright(x)
                else:
                    bracelet.crossleft(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
        for x in range(strings-1):
            if x%2 == 0:
                if x != strings-1:
                    bracelet.crossright(x)
                else:
                    bracelet.crossleft(x)
        for x in range(strings-1):
            if x%2 != 0:
                if x <= (strings-1)/2:
                    bracelet.crossleft(x)
                else:
                    bracelet.crossright(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
        for x in range(strings-1):
            if x%2 == 0:
                if x != 0:
                    bracelet.crossright(x)
                else:
                    bracelet.crossleft(x)
        for x in range(strings-1):
            if x%2 != 0:
                if x <= (strings-1)/2:
                    bracelet.crossright(x)
                else:
                    bracelet.crossleft(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
        loops += 1
        
def eyes1(strings = 4, distance = 10, velocity = 2):
    bracelet = knots(strings, distance, velocity)
    loops = 0 
    while loops < 1:
        #1
        for x in range(strings):
            if x%2==0:
                bracelet.turnleft(x)
        #2
        for x in range(strings-1):
            if x%2!=0:
                bracelet.turnright(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
        #3
        for x in range(strings):
            if x%2==0:
                bracelet.turnleft(x)
        #4
        for x in range(strings-1):
            if x%2!=0:
                bracelet.turnleft(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)      
        #5
        for x in range(strings):
            if x%2==0:
                bracelet.turnright(x)
        #6
        for x in range(strings-1):
            if x%2!=0:
                bracelet.turnright(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)
        #7
        for x in range(strings):
            if x%2==0:
                bracelet.turnright(x)
        #8
        for x in range(strings-1):
            if x%2!=0:
                bracelet.turnleft(x)
        for x in range(strings):
                if x == 0 or x == strings-1:
                    bracelet.edge(x)   
        loops += 1
import turtle
turtle.exitonclick()
