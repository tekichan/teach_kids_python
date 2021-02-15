from turtle import *

# Create a list of tuples of Radius and Color 
# Each element of the list is a tuple of Radius and Color
radii_colors_list = [
    (80, 'red')
    , (70, 'orange')
    , (60, 'yellow')
    , (50, 'green')
    , (40, 'blue')
    , (30, 'cyan')
    , (20, 'violet')
    , (10, 'white')
]

# Loop the list by for-loop. In each loop, an element is put to radius_color variable
for radius_color in radii_colors_list:
    fillcolor(radius_color[1])  # Take the second element (Color) to fill the color
    begin_fill()
    circle(radius_color[0])     # Take the first element (Radius) to draw a circle
    end_fill()

exitonclick()           # Exit when you click the screen