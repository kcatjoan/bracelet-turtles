import turtle
def doublechevronnet(strings, distance):
  turtledict = {'turtle' + str(anynum): {turtle.Turtle()} for anynum in range(strings)}
  print(turtledict)
  turtle.exitonclick()
doublechevronnet(5,40)
