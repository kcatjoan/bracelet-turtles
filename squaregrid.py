import turtle
wn = turtle.Screen()
robin = turtle.Turtle()
ldistances = [10, 20, 50, 100]
robin.up()
for x in ldistances:
  timesrun = 0
  while timesrun < 4:
    robin.forward(x)
    robin.dot()
    robin.left(90)
    timesrun = timesrun + 1
robin.goto(0,0)
turtle.exitonclick()
