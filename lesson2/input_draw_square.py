from turtle import *
user_answer = input('How long is your square side? ')       # Ask for the length of side
side_length = int(user_answer)                              # Convert user_answer to an integer

right_angle = 90        # Define the degree of right angle
square_color = 'red'    # Define the color of the square

fillcolor(square_color) # Request to use the color to fill
begin_fill()            # Begin to fill
forward(side_length)
right(right_angle)
forward(side_length)
right(right_angle)
forward(side_length)
right(right_angle)
forward(side_length)
end_fill()              # End to fill

exitonclick()