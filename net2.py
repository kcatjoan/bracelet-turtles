import turtle

def diagline(strings, distance):
  turtlesdefined = 0
  turtlesweaving = 0
  turtlenamelist = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
  #This program maxes out at 10 strings. Do not use more
  #distancemoved = 0. You don't need this because turtle.position() exists. I don't know how to use it yet
  while turtlesdefined < strings:
    for turtlename in turtlenamelist:
      #Position depending on how many strings already exist.
      turtlename.forward(turtlesdefined*distance)
      turtlesdefined += 1
  while turtlesweaving < strings:
    for turtlename in turtlenamelist:
      turtlename.right(45)
      #go forward, dotting at intervals, until y-position reaches the edge of the bracelet
      print(turtle.position()) #Temporary-- make sure I know what turtle.position() does
      #turtlename.left.90
      #forward again until the other edge of the bracelet
      turtlesweaving += 1
      
      
diagline(5, 40)
turtle.exitonclick()


#For the patterns I'll need another loop checking at what x-axis all turtles are in their original columns. I'm guessing the tricky thing will be not just quitting 
#whenever a string doubles back. For now it can be infinite
