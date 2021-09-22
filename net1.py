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
#the program shouldn't need the input of each turtle-- it should define turtles according to number of strings, and position them according to distance.
#I think I need to start over.
turtle.exitonclick()
