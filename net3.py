import turtle
def doublechevronnet(strings, distance):
#   turtledict = {"line" + str(anynum): {turtle.Turtle()} for anynum in range(strings)}
#   print(turtledict)
#   for eachturtle in turtledict:
#     print(type(turtledict[eachturtle]))
#     turtledict[eachturtle].forward(40)  
  turtlesdefined = 0
  definedturtles = []
  turtlesweaving = 0
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
      #positions turtles, leaves "rightedge" as the farthest distance traveled
    #(FIGURE  OUT HOW TO HAVE THE TURTLES SPLIT):
    currentxpos = list(turtlename.pos())[0]
  while 5 == 5:
    for turtlename in definedturtles:
      if 0.0 < currentxpos < rightedge:
        turtlename.forward(distance)
      else:
        turtle.right(90)

      
  turtle.exitonclick()
doublechevronnet(5,40)
