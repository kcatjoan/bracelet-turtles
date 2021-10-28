import turtle
import math
testall = False
stringdictionary = {}
stringsdefined = 0
def double_chevron_net(strings, distance, velocity = 8, rows = 5):
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
            turtlename.speed(velocity)
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

def candystripe(strings, distance, length = 6, velocity = 2):
    #position turtles in colors at columns
    hypdist = math.sqrt(2*(distance**2))
    columndict = {}
    columnsdefined = 0
    turtlesdefined = 0
    turtledictionary = {}
    timesrun = 0
    colorlist = ["red", "orange", "yellow", "green", "blue", "purple"]
    for number in range(strings):
        turtledictionary[str(number)] = turtle.Turtle()
    for eachturtle in turtledictionary:
        turtlename = turtledictionary[eachturtle]
        turtlename.color(colorlist[turtlesdefined])
        turtlename.speed(velocity)
        positiondistance = turtlesdefined*distance
        turtlename.forward(positiondistance) 
        turtlename.right(45)
        turtlename.rightfacing = True
        columndict[turtlename] = turtlesdefined
        turtlesdefined += 1 
    row = 0
    while timesrun < length:
        if row == 0:
            #Set alternating turtles facing alternating ways, with even facing right and odd facing left
            for key in turtledictionary:
                turtlename = turtledictionary[key]
                if int(key)%2 == 0:
                    if turtlename.rightfacing == False:
                        turtlename.left(90)
                    turtlename.rightfacing = True
                else:
                    if turtlename.rightfacing == True:
                        turtlename.right(90)
                    turtlename.rightfacing = False
        for key in turtledictionary:
            turtlename = turtledictionary[key]
            #At edge, go down vertically and turn inward
            if columndict[turtlename] == 0 and turtlename.rightfacing == False:
                turtlename.left(45)
                turtlename.forward(distance)
                turtlename.left(45)
                turtlename.rightfacing = True
            elif columndict[turtlename] == strings-1 and turtlename.rightfacing == True:
                turtlename.right(45)
                turtlename.forward(distance)
                turtlename.right(45)
                turtlename.rightfacing = False
            #Moves all turtles forward
            turtlename.speed(velocity)
            if turtlename.rightfacing == False:
                turtlename.forward(hypdist)
                columndict[turtlename] -= 1
            else:
                turtlename.forward(hypdist/2)
                turtlename.dot()
                turtlename.forward(hypdist/2)
                columndict[turtlename] += 1

        row += 1
        timesrun += 1
    turtle.exitonclick()
#run code
if (__name__ == "__main__"):
    double_chevron_net(4, 60)
    candystripe(4, 60, 20, 3)
