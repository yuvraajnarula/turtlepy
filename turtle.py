import turtle
#windows
wn = turtle.Screen() 
wn.bgcolor("black")
#colors
colors = ["violet", "indigo", "blue","green","yellow","orange","red"]
draw = turtle.Turtle()
for x in range(360):
    draw.pencolor(colors[x % 7])
    draw.width(x/100 + 1)
    draw.forward(x)
    draw.left(59)
turtle.done()