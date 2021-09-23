import turtle
def doublechevronnet(strings, distance):
  turtledict = {"line" + str(anynum): {turtle.Turtle()} for anynum in range(strings)}
  print(turtledict)
  for eachturtle in turtledict:
    print(type(eachturtle))
    #eachturtle.forward(40)
  turtle.exitonclick()
doublechevronnet(5,40)
