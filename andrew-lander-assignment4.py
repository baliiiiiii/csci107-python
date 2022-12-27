# -----------------------------------------+
# Andrew Lander                            |
# CSCI 107, Assignment 4                   |
# Last Updated: 10, 04, 20XX               |
# -----------------------------------------|
# Define and comment the two missing       |
# functions such that the desired Betsy    |
# Ross flag is drawn.                      |
# -----------------------------------------+

import turtle


# ---------------------------------------------------------------------------------------+
# draw_star turtle object, color, initial x coordinate, initial y coordinate             |
# This function creates a star, with each "arm" of the star being the "length" variable. |
# I'd draw it for you, but ASCII art of a star is above my artistic ability.             |
# ---------------------------------------------------------------------------------------+


def draw_star(flag,color,length,xcor,ycor):
    for i in range(5):
        flag.pendown()
        flag.color(color)
        flag.forward(length)
        flag.right(180 - 180/5)


# ------------------------------------------------------------------------------------------------------------------+
# draw_rectangle turtle object, color, horizontal length, vertical length, initial xcoordinate, initial ycoordinate |
# This function creates a rectangle in the top-left corner with the horizontal and vertical lengths mentioned. It   |
# usually looks like this:                                                                                          |
#           +---------horizontal_length-------------+                                                               |
#           |                                       | <---------- vertical_length                                   |
#           +---------------------------------------+                                                               |
# ------------------------------------------------------------------------------------------------------------------+


def draw_rectangle(flag, asdf, horizontal_len, vertical_len, xcor, ycor):
    flag.penup()
    flag.home()
    flag.color(asdf)
    flag.pencolor("black")
    flag.goto(xcor,ycor)
    flag.pendown()
    flag.begin_fill()
    for i in range(2):
        flag.forward(horizontal_len)
        flag.right(90)
        flag.forward(vertical_len)
        flag.right(90)
    flag.end_fill()


# -----------------------------------------+
# main (no parameters)                     |
# -----------------------------------------+


def main():
    window = turtle.Screen()
    
    flag = turtle.Turtle()
    flag.hideturtle()
    flag.speed(0) #thank you :)
    
    # initially, make the background of the entire flag red
    # the dimensions of the flag are 450 by 325
    # the upper left corner of the flag is at (-200, 175)
    draw_rectangle(flag, "red", 450, 325, -200, 175)

    # fill in the blue part in the upper left corner
    draw_rectangle(flag, "blue", 175, 175, -200, 175)

    # draw the three white strips to the right of the blue part
    y = 150
    for _ in range(3):
        draw_rectangle(flag, "white", 275, 25, -25, y)
        y -= 50

    # draw the three white stripes below the blue part
    for _ in range(3):
        draw_rectangle(flag, "white", 450, 25, -200, y)
        y -= 50
    
    # draw the 13 white stars
    flag.penup()
    flag.goto(-185, 95)
    for _ in range(13):
        # each of the 5 lines of the star is 20 pixels
        # the left side of the horizontal line is at (flag.xcor(), flag.ycor())
        flag.begin_fill()
        draw_star(flag, "white", 20, flag.xcor(), flag.ycor())
        flag.end_fill()
        flag.penup()
        flag.forward(140)
        flag.right(180 - 180/13)
    window.exitonclick()

# -----------------------------------------+

main()