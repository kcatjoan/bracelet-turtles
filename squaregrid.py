import turtle
wn = turtle.Screen()
robin = turtle.Turtle()
ldistances = [10, 20, 50, 100]
timesrun = 0 

robin.up()
robin.speed(3)
for x in ldistances:
  while timesrun >= 8:
    robin.forward(x)
    robin.dot()
    robin.left(90)
    timesrun += 1
robin.goto(0,0)
