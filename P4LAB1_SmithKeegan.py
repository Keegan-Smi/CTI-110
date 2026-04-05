import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
t = turtle.Turtle()
t.color("green")
t.pensize(2)

# -----------------------
# Draw Square (using for loop)
# -----------------------
t.penup()
t.goto(-50, -50) # position for square
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

# -----------------------
# Draw Triangle Roof (using while loop)
# -----------------------
t.penup()
t.goto(-50, 50) # top of square
t.pendown()

t.color("green")

t.begin_fill()

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

t.end_fill()

# Hide turtle and finish
t.hideturtle()
turtle.done()