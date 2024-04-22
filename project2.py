import turtle
import turtle as t
import TurtleClass

# import Turtle Module
# Establish 4 turtles
# Make turtles have coordinates
# turtle will compare to each others coordinates
# turtles will run from each other

# I need to establish a class for turtle.
# I need to simultaneously change the turtles position based on turtles nearby

# Maybe I just set up a Sphere in a 3d Axis

# Write the sphere algorithm
# should be along the line of 4*pi*r^2
# center of sphere is at (x - a)² + (y - b)² + (z - c)² = r²
# the center can be used to calculate the distance the dot must be away from the sphere or how close it needs to be
# d=√((x2 – x1)² + (y2 – y1)² + (z2 - z1)) Will find the distance between 2 points Z will transparency.

turtle.colormode(255)
# Establish Background
wn = t.Screen()
wn.bgcolor("black")

# center of sphere Attributes
nucleus = t.Turtle()
nucleus.shape("circle")
nucleus.turtlesize(.1)

# outside points of sphere attributes
particle = t.Turtle()
particle.shape("circle")
particle.turtlesize(.1)

# Get Center information
# radius = int(input("Radius:"))
radius = 100


# Find real position
# ((particleX - centerX)**2) + ((particleY - centerY)**2) + ((particleZ - CenterZ)**2) = radius**2

particleX = 0
particleY = 0
particleZ = 100

#
particleZPercent = float(particleZ / radius)
colorCoordZ = int(82 * particleZPercent)
print(colorCoordZ)
particle.color(colorCoordZ, 0, 0)



# establish the center Coordinates.
centerX = 0
centerY = 0
centerZ = 0

# Display effect to render Z coordinate
colorCoordZ = centerZ + 82
nucleus.color(colorCoordZ, 0, 0)

while True:
    nucleus.setposition(centerX,centerY)
    particle.up()
