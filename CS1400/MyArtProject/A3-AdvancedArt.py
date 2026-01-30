# The starter code:
# provides the template for creating a turtle screen
# gives that turtle with some basic settings.
# calls the draw_square method with that turtle.
# places all of the “main” actions in the main function and calls the main function when the file is executed.
import turtle
wn = turtle.Screen()
my_turtle = turtle.Turtle()

def signature(drawing_turtle, x_pos, y_pos, radius):
    draw_circle(drawing_turtle, x_pos, y_pos, radius)