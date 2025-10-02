import turtle
wn = turtle.Screen()
wn.title("lol")
# Set up the turtle
t = turtle.Turtle()
wn.bgcolor("#000000")
t.begin_fill()
t.color("#00FF00")
t.circle(50, steps=3)
t.circle(60, steps=4)
t.end_fill()
turtle.Screen().exitonclick()