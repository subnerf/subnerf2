import turtle
wn = turtle.Screen()
wn.title("lol")
# Set up the turtle
t = turtle.Turtle()
wn.bgcolor("black")
t.begin_fill()
t.color("white")
#t.circle(50, steps=3)
t.color("#ff0000")
t.circle(60)
t.left(20)
t.circle(60, extent=180)

wn.bgpic("C:/Users/klase/Downloads/subnerf2 (3)/subnerf2/Untitled.gif")

turtle.Screen().exitonclick()