from turtle import *

right_angle = 90        # Define the degree of right angle

# Get the length of side from the list of numbers
for side_length in [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]:
    forward(side_length)
    right(right_angle)
    forward(side_length)
    right(right_angle)
    forward(side_length)
    right(right_angle)
    forward(side_length)

exitonclick()           # Exit when you click the screen