class knots:
    stringdictionary = {}
    stringsdefined = 0
    turtledictionary = {}
    turtlesdefined = 0
    stringnumber = 0
    turtleonstring = {}
    turtledictionary = {}

    def __init__(self, strings, distance, dotsize = 4, velocity = 2):
        import turtle
        import math
        turtle.setworldcoordinates(-50, -200, 200, 50)
        knots.hypdist = math.sqrt(2*(distance**2))
        knots.columndict = {}
        knots.distance = distance
        knots.dotsize = dotsize
        turtlesdefined = 0
        timesrun = 0
        colorlist = ["red", "orange", "gold", "green", "blue", "purple", "red", "orange", "gold", "green", "blue", "purple"]
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
        print(knots.columndict)
        row = 0
    # def facingturtles(self, stringnumber):
    #     sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
    #     leftturtle, rightturtle = sortcolumns[stringnumber], sortcolumns[stringnumber+1]
    #     if leftturtle.rightfacing == False:
    #         leftturtle.left(90)
    #         leftturtle.rightfacing = True
    #     if rightturtle.rightfacing == True:
    #         rightturtle.right(90)
    #         rightturtle.rightfacing = False
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
        # sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        # print(sortcolumns)

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
        # sortcolumns = sorted(knots.columndict, key = lambda x:knots.columndict[x])
        # print(sortcolumns)
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
def diagAltStripes():  
    bracelet = knots(6, 10)
    while True:
        bracelet.crossright(0), bracelet.crossright(2), bracelet.crossright(4)
        bracelet.edge(0), bracelet.turnleft(1), bracelet.turnleft(3), bracelet.edge(5)
diagAltStripes()
# strings = 6
# bracelet = knots(strings, 5)
# loops = 0
# while True:
#     if loops%2 == 0:
#         lines = 0
#         while lines <= 5:
#             for x in range(strings-1):
#                 if x%2 == 0:
#                     if x <= strings/2:
#                         bracelet.crossright(x)
#                     else:
#                         bracelet.crossleft(x)
#             for x in range(strings-1):
#                 if x%2 != 0:
#                     bracelet.crossright(x)
#         lines += 1
#     for x in range(strings-1):   
#         if x == 0 or x == strings-1:
#             bracelet.edge(x)
#     loops += 1
