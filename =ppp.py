import turtle
wn = turtle.Screen()
wn.title("lol")
# Set up the turtle
t = turtle.Turtle()
wn.bgcolor("#000000")
t.begin_fill()
t.color("#00FF00")
t.speed(10)
t.circle(50, steps=3)# Draws a triangle with side length approximately 86.60
t.circle(60, steps=4)# Draws a square with side length approximately 84.85
t.circle(70, steps=5)# Draws a pentagon with side length approximately 82.35
t.circle(80, steps=6)# Draws a hexagon with side length approximately 80.00
t.circle(90, steps=7)# Draws a heptagon with side length approximately 78.00
t.circle(100, steps=8)# Draws an octagon with side length approximately 76.39
t.circle(110, steps=9)# Draws a nonagon with side length approximately 75.00
t.circle(120, steps=10)# Draws a decagon with side length approximately 73.53
t.circle(130, steps=11)# Draws a hendecagon with side length approximately 72.00
t.circle(140, steps=12)# Draws a dodecagon with side length approximately 71.03
t.circle(150, steps=13)# Draws a triskaidecagon with side length approximately 70.00
turtle.Screen().exitonclick()