import turtle
def doublechevronnet(strings, distance): 
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
    print(type(currentxpos))
#   while 5 == 5:
#     for turtlename in definedturtles:
#       if 0.0 < currentxpos < rightedge:
#         turtlename.forward(distance)
#       elif currentxpos == rightedge:
#         turtlename.right(90)
#       elif currentxpos == 0.0:
#         turtlename.left(90)
  
#   turtle.exitonclick()
# doublechevronnet(5,40)
