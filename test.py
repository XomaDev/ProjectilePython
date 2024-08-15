import math

# Initial parameters
G = 9.8  # gravity in m/s^2
u = 20  # initial velocity in m/s
theta = math.radians(30)  # converting degrees to radians
t = 1.5  # time in seconds

# Calculate components of velocity
Ux = u * math.cos(theta)
Uy = u * math.sin(theta)

# Calculate positions at time t = 1.5 seconds
xPos = Ux * t
yPos = Uy * t - (0.5 * G * t ** 2)

# Print the results
print(f"x position at t = {t} seconds: {xPos:.2f} meters")
print(f"y position at t = {t} seconds: {yPos:.2f} meters")
