import turtle
line1 = turtle.Turtle()
numstrings = 5
timesrun = 0
def diagline(turtlename): 
  turtlename.right(45)
  while timesrun < numstrings:
    turtlename.forward(40)
    turtlename.dot()
    timesrun += 1
    
diagline(line1)
turtle.exitonclick()
