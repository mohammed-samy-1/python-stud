import turtle

# Create a turtle screen
wn = turtle.Screen()

# Create a turtle
t = turtle.Turtle()
t.speed(1)

# Turtle shell (draw a filled oval to give it a 3D effect)
t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.begin_fill()
t.left(90)
t.forward(200)
t.left(90)
t.circle(100, 180)
t.left(90)
t.forward(200)
t.left(90)
t.circle(100, 180)
t.end_fill()

# Turtle head
t.penup()
t.goto(0, 20)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(20)
t.end_fill()

# Eyes
t.penup()
t.goto(30, 40)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(-30, 40)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# Nose
t.penup()
t.goto(0, 20)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(3)
t.end_fill()

# Mouth
t.penup()
t.goto(5, 10)
t.pendown()
t.color("black")
t.left(90)
t.circle(5, 180)

# Legs
t.penup()
t.goto(40, -100)
t.pendown()
t.color("green")
t.begin_fill()
t.left(90)
t.forward(20)
t.left(90)
t.forward(15)
t.left(90)
t.forward(20)
t.end_fill()

t.penup()
t.goto(-60, -100)
t.pendown()
t.color("green")
t.begin_fill()
t.left(90)
t.forward(20)
t.left(90)
t.forward(15)
t.left(90)
t.forward(20)
t.end_fill()

# Close the turtle graphics window when clicked
wn.exitonclick()
