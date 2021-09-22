import turtle
wn = turtle.Screen()
robin = turtle.Turtle()
ldistances = [10, 20, 50, 100]
timesrun = 0 

robin.up()
#robin.speed(8)
#while timesrun >= 8:
  for x in ldistances:
    robin.forward(x)
    robin.dot()
    robin.left(90)
    timesrun = timesrun + 1
robin.goto(0,0)
turtle.exitonclick()
