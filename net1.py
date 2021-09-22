import turtle
line1 = turtle.Turtle()
increments = 5
timesrun = 0

line1.right(45)
while timesrun < increments:
  line1.forward(40)
  line1.dot()
  timesrun += 1
turtle.exitonclick()
