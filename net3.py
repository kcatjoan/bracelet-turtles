def double_chevron_net(strings, distance):
#import the things
    import turtle
    turtledictionary = {}
    row = 1
    stuckturtles = 0
    stringdictionary = {}
    stringsdefined = 0
    turtlesdefined = 0
    stringnumber = 0
    timesiterated = 0
    turtleonstring = {}
    testall = False
    testrightmove = True
#going by the stringnumber and the distance, set:
    #the strings (a dictionary: keys are numbers and values are positions)
    for string in range(strings):
        stringdictionary[string] = stringsdefined*distance
        stringsdefined += 1
    for number in range(2*strings):
        turtledictionary["Turtle number " + str(number)] = turtle.Turtle()
        #turtledictionary: {'Turtle number 0': <turtle.Turtle object at 0x10b9a78b0>, 'Turtle number 1': <turtle.Turtle object at 0x10bafdca0>, 'Turtle number 2': <turtle.Turtle object at 0x10bafdfd0>, 'Turtle number 3': <turtle.Turtle object at 0x10bafdc70>, 'Turtle number 4': <turtle.Turtle object at 0x10bb280d0>, 'Turtle number 5': <turtle.Turtle object at 0x10bb28220>, 'Turtle number 6': <turtle.Turtle object at 0x10bb28370>, 'Turtle number 7': <turtle.Turtle object at 0x10bb284c0>, 'Turtle number 8': <turtle.Turtle object at 0x10bb28610>, 'Turtle number 9': <turtle.Turtle object at 0x10bb28760>}
    for eachturtle in turtledictionary:
        turtlename = turtledictionary[eachturtle]
        turtlename.up()
        if turtlesdefined % 2 == 0:
            positiondistance = turtlesdefined*distance/2
            turtlename.rightfacing = True
            turtlename.color("red") 
            if turtlesdefined > 1:
                stringnumber += 1
        else:
            turtlename.rightfacing = False
            # timesiterated += 1 
        turtlename.forward(positiondistance) 
        turtlename.down()
        if turtlename.rightfacing == True:
            turtlename.left(45)
        else:
            turtlename.right(45)
        turtleonstring[turtlename] = stringnumber
        turtlesdefined += 1  
    # print(timesiterated)
        # print("Stringnumber " + str(stringnumber) + " is stringdictionary definition " + str(stringdictionary[stringnumber]))
        #This bit is supposed to make sure that each stringnumber can be used to refer to a position. 
        #Because then I can set dictionaries where the key is the turtlename and the value is the stringnumber, 
        #and then use that value to refer to a different dictionary where the value is the position.
        #Turtlename[stringnumber] can connect to stringdictionary[distance].
        #Why not use turtlename[distance]?
        #because aaaaa
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
        if turtleonstring[turtlename] == 1:
            print(str(turtlename) + " row is " + str(row))

    while stuckturtles < strings:
        # turtlename = turtledictionary["Turtle number 0"]
        for eachturtle in turtledictionary:
            turtlename = turtledictionary[eachturtle]
            if turtlename.rightfacing == True:
                # print("Undergoing rightmove")
                # print(str(turtleonstring[turtlename]) + " is (str(turtleonstring[turtlename])")
                rightmove(turtlename)
            elif turtlename.rightfacing == False:
                # print("Undergoing leftmove")
                # print(str(turtleonstring[turtlename]) + " is (str(turtleonstring[turtlename])")
                leftmove(turtlename)
            if turtleonstring[turtlename] == strings:
                turtlename.rightfacing = False
                leftmove(turtlename)
                # print("verily an edge")
            elif turtleonstring[turtlename] == 0:
                turtlename.leftfacing = True
                rightmove(turtlename)
                print("yes indeed an edge")
            # else:
            #     print(str(turtlename) + " is stuck at " + str(turtleonstring[turtlename]))
            #     stuckturtles += 1
        row += 1
#describe where to apply rightmove and leftmove
#run code
if (__name__ == "__main__"):
    double_chevron_net(5,20)
