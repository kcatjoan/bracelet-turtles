import turtle
import math
testall = False
rows = 5
stringdictionary = {}
stringsdefined = 0
def double_chevron_net(strings, distance):
#import the things
    window = turtle.Screen()
    turtledictionary = {}
    row = 1
    stuckturtles = 0
    turtlesdefined = 0
    stringsdefined = 0
    stringnumber = 0
    turtleonstring = {}
    testrightmove = False
    turtle.setworldcoordinates(-5*distance, -20*distance, 20*distance, 5*distance)
#going by the stringnumber and the distance, set:
    #the strings (a dictionary: keys are numbers and values are positions)
    for string in range(strings):
        stringdictionary[string] = stringsdefined*distance
        stringsdefined += 1
    for number in range(2*strings):
        turtledictionary["Turtle number " + str(number)] = turtle.Turtle()
    #position turtles
    for eachturtle in turtledictionary:
        turtlename = turtledictionary[eachturtle]
        turtlename.up()
        if turtlesdefined % 2 == 0:
            positiondistance = turtlesdefined*distance/2
            turtlename.rightfacing = True
            # turtlename.color("red") 
            if turtlesdefined > 1:
                stringnumber += 1
        else:
            turtlename.rightfacing = False
        turtlename.forward(positiondistance) 
        turtlename.down()
        if turtlename.rightfacing == True:
            turtlename.left(45)
        else:
            turtlename.right(45)
        turtleonstring[turtlename] = stringnumber
        turtlesdefined += 1  
#define rightmove and leftmove 
    def turnright(turtlename):
        if testall == True:
                print(str(turtlename) + "is the turtle undergoing Turnright. Its current string is " + str(turtleonstring[turtlename]) + " and its rightfacing is " + str(turtlename.rightfacing) + "and its row is " + str(row))
        turtleonstring[turtlename] += 1
        turtlename.goto(stringdictionary[turtleonstring[turtlename]], -row*distance)
        if testall == True:
                print(str(turtlename) + "is the turtle undergoing Turnright. Its new string is " + str(turtleonstring[turtlename]) + "and its row is " + str(row))
    def leftmove(turtlename):
        turtlename.rightfacing = False
        if turtleonstring[turtlename] > 0:
            if testall == True:
                print(str(turtlename) + "is the turtle undergoing Leftmove. Its current string is " + str(turtleonstring[turtlename]) + " and its rightfacing is " + str(turtlename.rightfacing) + " and its row is " + str(row))
            turtleonstring[turtlename] -= 1
            turtlename.goto(stringdictionary[turtleonstring[turtlename]], -row*distance)
            if testall == True:
                print(str(turtlename) + "is the turtle undergoing Leftmove. Its new string is " + str(turtleonstring[turtlename]) + " and its row is " + str(row))
        else:
            if testall == True:
                print(str(turtlename) + " is at the left edge")
            turnright(turtlename)
    def rightmove(turtlename):
        turtlename.rightfacing = True
        if turtleonstring[turtlename] + 1 < strings:
            if testall == True or testrightmove == True:
                print(str(turtlename) + "is the turtle undergoing Rightmove. Its current string is " + str(turtleonstring[turtlename]) + " and its rightfacing is " + str(turtlename.rightfacing) + " and its row is " + str(row))
            turtleonstring[turtlename] += 1
            turtlename.goto(stringdictionary[turtleonstring[turtlename]], -row*distance)
            if testall == True or testrightmove == True:
                print(str(turtlename) + "is the turtle undergoing Rightmove. Its new string is " + str(turtleonstring[turtlename]) + " and its row is " + str(row))
        else:
            if testall == True or testrightmove == True:
                print(str(turtlename) + " is at the right edge")
            leftmove(turtlename)
        if turtleonstring[turtlename] == 1 and testall == True:
            print(str(turtlename) + " row is " + str(row))

    while row < rows:
        for eachturtle in turtledictionary:
            turtlename = turtledictionary[eachturtle]
            turtlename.speed(8)
            turtlename.hasmoved = False
            if turtlename.rightfacing == True and turtlename.hasmoved == False:
                rightmove(turtlename)
                turtlename.hasmoved = True
            elif turtlename.rightfacing == False and turtlename.hasmoved == False:
                leftmove(turtlename)
                turtlename.hasmoved = True
            if turtleonstring[turtlename] == strings:
                turtlename.rightfacing = False
                leftmove(turtlename)
                turtlename.hasmoved = True
            elif turtleonstring[turtlename] == 0:
                turtlename.rightfacing = True
                if turtlename.hasmoved == False:
                    rightmove(turtlename)
                turtlename.hasmoved = True
        row += 1
    # turtle.exitonclick

def candystripe(strings, distance):
    #position turtles in colors at columns
    hypdist = math.sqrt(2*(distance**2))
    columndict = {}
    columnsdefined = 0
    turtlesdefined = 0
    turtledictionary = {}
    timesrun = 0
    colorlist = ["red", "orange", "yellow", "green", "blue", "purple"]
    for number in range(strings):
        turtledictionary["Turtle number " + str(number)] = turtle.Turtle()
    for eachturtle in turtledictionary:
        turtlename = turtledictionary[eachturtle]
        turtlename.color(colorlist[turtlesdefined])
        positiondistance = turtlesdefined*distance
        turtlename.rightfacing = True
        turtlename.forward(positiondistance) 
        # if turtlesdefined < (strings - 1):
        #     turtlename.right(45)
        # else:
        #     turtlename.right(135)
        #     turtlename.rightfacing == False
        turtlename.right(45)
        turtlename.rightfacing = True
        columndict[turtlesdefined] = turtlename
        turtlesdefined += 1 
    # A straight right knot works by swapping the positions of the two strings involved,
    # and moving them both down one row, while the string on the right makes a "dot knot" on top of the other string.
    # My code should work the same way.
    # Take X turtle, and the turtle to its immediate right
    # Move Y turtle to the left, down to the next row
    # X turtle moves until it intersects the Y string, dots, and continues right down to the next row.
    # I'll start by trying to get it to recognize pairs of turtles. I'll start with even numbers of strings and then
    # figure out how to deal with odd. 

    #A turtle and its immediate right.
    while timesrun < 3:
        for item in columndict:
            #only the odd-numbered strings, though:
            if item % 2 == 0:
                if item < (len(columndict) - 1):
                #that is, if it's not the second-to-rightmost string:
                    (leftturtle, rightturtle) = (columndict[item], columndict[item + 1])
                    rightturtle.right(90)
                    rightturtle.forward(hypdist)
                    leftturtle.forward(hypdist/2)
                    leftturtle.dot()
                    leftturtle.forward(hypdist/2)
            #Columndict: Dictionary in which 1 : turtle 1
                    if timesrun < len(columndict) - 1:
                        (columndict[timesrun], columndict[timesrun + 1]) = (rightturtle, leftturtle)    
                        #there has GOT to be a better way to do this   
                #Turn the left edge around
                leftestturtle = columndict[0]
                leftestturtle.left(45)
                timesrun += 1

    turtle.exitonclick()
#run code
if (__name__ == "__main__"):
    double_chevron_net(4, 160)
    candystripe(4, 160)
