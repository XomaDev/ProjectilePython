import math
import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.goto(-400, -350)
t.pendown()

BLOCK = 25
G = 9.8 # gravity, m/s^2

u = 20 # m/s
x_deg = 50
x = math.radians(x_deg)

Uy = u * math.sin(x)
Ux = u * math.cos(x)

# max height = ((u sin(x))^2) / g
max_height = (Uy ** 2) / (2 * G) # meters

# max time = 2u sin(x) / g
time_flight = 2 * Uy / G

t.setheading(x_deg)

# pos(x) = u cos(x) t
# pos(y) = u sin(x) t - 1/2gt^2

time_ms = int(time_flight * 1000)

xLast = 0
yLast = 0
for time in range(0, time_ms + 1):
    time_sec = time / 1000.0
    xPos = Ux * time_sec
    yPos = Uy * time_sec - (0.5 * G * time_sec ** 2)

    xDiff = (xPos - xLast) * BLOCK
    yDiff = (yPos - yLast) * BLOCK

    current_pos = t.pos()

    t.goto(current_pos[0] + xDiff, current_pos[1] + yDiff)

    xLast = xPos
    yLast = yPos


turtle.done()