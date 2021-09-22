import turtle
line1 = turtle.Turtle()
numstrings = 5
def diagline(turtlename): 
  timesrun = 0
  turtlename.right(45)
  while timesrun < numstrings:
    turtlename.forward(40)
    turtlename.dot()
    timesrun += 1
    
diagline(line1)
turtle.exitonclick()
