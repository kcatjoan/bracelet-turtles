import turtle

def diagline(strings, distance):
  turtlesdefined = 0
  turtlesweaving = 0
  [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10] = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
            #There's gotta be a better way to do that.
  turtlenamelist = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
            #This program maxes out at 10 strings. Do not use more
            #distancemoved = 0. You don't need this because turtle.position() exists. I don't know how to use it yet
  #All variables have been set.
  for turtlename in turtlenamelist:
    if turtlesdefined <= strings:  
      turtlename.forward(turtlesdefined*distance)
      edge = list(turtlename.position())[0]
      print(edge)
      turtlesdefined += 1
  for turtlename in turtlenamelist:
    if turtlesweaving < strings:
      turtlename.right(45)
      #go forward, dotting at intervals, until x-position reaches the edge of the bracelet. DON'T YET KNOW HOW TO FORMAT W. POSITION()
    turtlex = list(turtlename.position())
    print(turtlex[0])
    if turtlex < edge:
   #   print(turtlename.position())
      turtlename.forward(45)
 #     #45 isn't the right number but it's fine for now
 #     turtlename.right(90)
 #     if turtlename.position()[0] > 0:
 #      turtlename.forward(45)
      turtlesweaving += 1
      
      
diagline(5, 40)
turtle.exitonclick()


#For the patterns I'll need another loop checking at what x-axis all turtles are in their original columns. I'm guessing the tricky thing will be not just quitting 
#whenever a string doubles back. For now it can be infinite
