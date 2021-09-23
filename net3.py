import turtle
import math
def doublechevronnet(strings, distance): 
  horizontaldistance = (math.sqrt((distance*distance)/2))
  print(str(horizontaldistance) + " is one side of an isosceles right triangle whose hypotenuse is " + str(distance))
  turtlesdefined = 0
  definedturtles = []
  turtlesweaving = 0
  stuckturtles = 0
  dotsmade = 0
  [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10] = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
  turtlenamelist = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
  #All variables have been set.
  
  for turtlename in turtlenamelist:
    turtlename.up()
    if turtlesdefined <= strings: 
      definedturtles.append(turtlename)
      turtlename.forward(turtlesdefined*distance)
      rightedge = list(turtlename.pos())[0]
      turtlename.down()
      turtlename.right(45)
      turtlesdefined += 1
      if turtlename not in definedturtles:
        del turtlenamelist[turtlename]
      #positions turtles, leaves "rightedge" as the farthest distance traveled
    #(ALSO HAVE THE TURTLES SPLIT):
  print(len(definedturtles))
  while stuckturtles < 10:
    for turtlename in definedturtles:
      currentxpos = list(turtlename.pos())[0]
      currentypos = list(turtlename.pos())[1]
      if 0.0 < currentxpos < rightedge:
          turtlename.forward(distance)
      elif currentxpos >= rightedge:
        turtlename.right(90)
        turtlename.forward(distance)
      elif currentxpos <= 0.0 and currentypos == 0.0:
        turtlename.forward(distance)
      elif currentxpos <= 0.0:
        turtlename.left(90)
        turtlename.forward(distance)  
      else:
        stuckturtles += 1
      
#         turtlename.left(45)
#         turtlename.forward(distance)
  
  turtle.exitonclick()
doublechevronnet(5,40)
