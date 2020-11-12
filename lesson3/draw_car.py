from turtle import *
right_angle = 90        # Define the degree of right angle
car_length = 200       # Define the length of the car
car_height = 50         # Define the height of the car
wheel_size = 30         # Define the size of the wheels
wheel_position = 50     # Define the position of the wheels
# Determine color by inputted gender
car_color = 'pink'
gender = input('Are you male or female? ')
if gender == 'male':
    car_color = 'blue'
# Draw a car body
fillcolor(car_color) 
begin_fill()            
forward(car_length)
right(right_angle)
forward(car_height)
right(right_angle)
forward(car_length)
right(right_angle)
forward(car_height)
end_fill()
# Draw two wheels
penup()                 # Pen Up. Do not draw when moving
back(car_height)        # Move backward
left(right_angle)       # Turn left
back(wheel_position)
pendown()               # Pen Down. Continue to draw when moving
circle(wheel_size)      # Draw a circle as a wheel
penup()
pendown()
back(car_length - wheel_position - wheel_position)  # Leave wheel_position long from two ends
circle(wheel_size)
exitonclick()