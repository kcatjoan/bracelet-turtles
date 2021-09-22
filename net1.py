import turtle
def diagline(turtlename, distance): 
  timesrun = 0
  turtlename.right(45)
  while timesrun < numstrings:
    turtlename.forward(distance)
    turtlename.dot()
    timesrun += 1

line1 = turtle.Turtle()
line2 = turtle.Turtle()
numstrings = 5
    
diagline(line1, 40)
line2.forward()
turtle.exitonclick()
