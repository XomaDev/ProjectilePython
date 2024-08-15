import math
import turtle

screen = turtle.Screen()

screen_width = screen.window_width()
screen_height = screen.window_height()

screen.setup(width=1.0, height=1.0)

screen.title("Projectile path")
canvas_width = 800
canvas_height = 800
screen.screensize(canvas_width, canvas_height)

t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.goto(-800, -400)
t.pendown()

BLOCK = 25
G = 9.8 # gravity, m/s^2

u = float(input("Initial velocity (m/s): "))
x_deg = float(input("angle of projection (degree): "))
x = math.radians(x_deg)

Uy = u * math.sin(x)
Ux = u * math.cos(x)

# max height = ((u sin(x))^2) / g
max_height = (Uy ** 2) / (2 * G) # meters

print("Max height", max_height, "meters")

# max time = 2u sin(x) / g
time_flight = 2 * Uy / G
print("Time of flight", time_flight, "seconds")

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

    trajectory_angle = math.atan2(Uy - G * time_sec, Ux)
    #print(time_sec, trajectory_angle)
    t.setheading(math.degrees(trajectory_angle))

    current_pos = t.pos()
    t.goto(current_pos[0] + xDiff, current_pos[1] + yDiff)

    turtle.update()

    xLast = xPos
    yLast = yPos


turtle.done()