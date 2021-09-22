import turtle
wn = turtle.Screen()
robin = turtle.Turtle()
ldistances = [10, 20, 50, 100]

robin.up()
robin.speed(3)
for x in ldistances:
  robin.forward(x)
  robin.dot()
  robin.left(90)
robin.goto(0,0)
