import turtle

def diagline(strings, distance):
  turtlesdefined = 0
  turtlesweaving = 0
  [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10] = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
            #There's gotta be a better way to do that. Defines a bunch of turtles in order
  turtlenamelist = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
            #This program maxes out at 10 strings. Do not use more
  #All variables have been set.
  
  #For loop sets start position of each string
  for turtlename in turtlenamelist:
    if turtlesdefined <= strings:  
      turtlename.up
      turtlename.forward(turtlesdefined*distance)
      #sets edge of bracelet to each turtle end position, ideally leaving "edge" as the farthest distance traveled
      edge = list(turtlename.position())[0]
      turtlesdefined += 1
  print(edge)
  #sets string angles
  for turtlename in turtlenamelist:
    if turtlesweaving < strings:
      turtlename.right(45)
      turtlename.down
    #converts turtle position into list
    turtlex = list(turtlename.position())[0]
    print(turtlex)
    if turtlex < edge:
   #   print(turtlename.position())
      turtlename.forward(45)
 #     #45 isn't the right number but it's fine for now
      turtlename.right(90)
 #     if turtlename.position()[0] > 0:
      turtlename.forward(45)
      turtlesweaving += 1
      
      
diagline(5, 40)
turtle.exitonclick()


#For the patterns I'll need another loop checking at what x-axis all turtles are in their original columns. I'm guessing the tricky thing will be not just quitting 
#whenever a string doubles back. For now it can be infinite
