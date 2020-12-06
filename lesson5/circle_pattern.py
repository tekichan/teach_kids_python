from turtle import *

bgcolor("green")    # Define Background Color
pencolor("red")     # Define the color of Pen, i.e our pattern's color
pensize(10)         # Define the size of Pen, i.e. the width of our pattern's line

radius = 100        # Define the radius of each circle
turning_angle = 36  # Define how much the next circle turns away from the previous one.

# A counter of totally how much the angle is turned. It starts with zero.
total_turned_angle = 0

while total_turned_angle < 360:
    # While loop, when the total angle is less than 360, i.e a round.
    circle(radius)          # Draw a circle
    # Turn right after you finish a circle, to prepare the new position of the next circle.
    right(turning_angle)
    # Accumulate the turning angle into the counter
    total_turned_angle = total_turned_angle + turning_angle

exitonclick()           # Exit when you click the screen