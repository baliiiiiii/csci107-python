# -----------------------------------------+
# Andrew Lander                            |
# CSCI 107, Assignment 3                   |
# Last Updated: September 21, 2022         |  
# -----------------------------------------|
# This is a drawing of Aang when he's in   |
# the iceberg. It also has only an earth   |
# symbol - I was hoping to get all of them,|
# but I ran out of time. Oh well! :)       | 
# -----------------------------------------+

import turtle
#initial creation of objects
tortoise = turtle.Turtle()
tortoisex = int(100)
tortoisey = int(100)
tortoiseradius = int()
screen = turtle.Screen()
screen.screensize(600,400,"white")
#set to rgb color mode
screen.colormode(255)
#tortoise.hideturtle()
#drawing settings
tortoise.speed(0)
#color is bluish gray
tortoise.color(179,200,229)
tortoise.hideturtle()
#arrow related variables
overallarrowdistance = 17
bottomarrowdistance = 12
sidebitarrowdistance = 6 #name :(

#function so I don't have to ctrlc-ctrlv all day
def drawcircle():
    tortoise.penup()
    tortoise.setposition(tortoisex,tortoisey)
    tortoise.pendown()
    tortoise.begin_fill()
    tortoise.circle(tortoiseradius)
    tortoise.end_fill()

#function to make arrows scalable - should work because it's always moving a distance not scaling sides (hint: it didn't work)
#set x, y, manipulate entirely w angle by encapsulating all of it
def drawarrow():
    tortoise.setposition(tortoisex,tortoisey)
    tortoise.begin_fill()
    tortoise.pendown()
    tortoise.right(90)
    tortoise.forward(overallarrowdistance)
    tortoise.right(90)
    tortoise.forward(sidebitarrowdistance)
    tortoise.left(90 + 45) #:^)
    tortoise.forward(overallarrowdistance)
    tortoise.left(90)
    tortoise.forward(overallarrowdistance)
    tortoise.left(45 + 90)
    tortoise.forward(sidebitarrowdistance)
    tortoise.right(90)
    tortoise.forward(overallarrowdistance)
    tortoise.left(90)
    tortoise.forward(bottomarrowdistance)
    tortoise.end_fill()
    tortoise.penup()
    
#actual drawing - try to mostly use built in shapes and x-y coordinate setting
#for loops for drawing continuous rectangles with curved edges
#head
tortoiseradius = 40
drawcircle()
#left ear
tortoisex = tortoisex - 35
tortoisey = tortoisey + 23
tortoiseradius = 12
drawcircle()
#right ear
tortoisex = 135
tortoisey = 123
tortoisradius = 12
drawcircle()
#neck
tortoisex = 75
tortoisey = 90
tortoiseradius = 13
for i in range(9):
    tortoisex += 5
    drawcircle()
#left shoulder
tortoisex = 68
tortoisey = 53
tortoiseradius = 24
drawcircle()
#right shoulder
tortoisex = 132
tortoisey = 53
drawcircle()
#left arm before elbow
tortoisex = 30
tortoisey = 7
tortoiseradius = 15
for i in range(8):
    tortoisey += 7
    tortoisex += 3
    drawcircle()
#left arm after elbows 
tortoisex = 30
tortoisey = 9
for i in range(7):
    tortoisex += 3
    tortoisey -= 1
    drawcircle()
#right arm before elbow
tortoisex = 170
tortoisey = 7
for i in range(8):
    tortoisey += 7 
    tortoisex -= 3
    drawcircle()
#right arm after elbow
tortoisex = 170
tortoisey = 9
for i in range(7):
    tortoisex -= 3
    tortoisey -= 1
    drawcircle()
#straight line between elbow-elbow
tortoisex = 53
tortoisey = 2
for i in range(18):
    tortoisex += 5
    drawcircle()
#fill in torso
tortoisex = 100
tortoisey = 20
tortoiseradius = 50
drawcircle()
tortoisex = 70
tortoisey = 20
tortoiseradius = 20
drawcircle()
tortoisex = 130
drawcircle()
#abdomen (?)
tortoisex = 60
tortoisey = -25
tortoiseradius = 22
for i in range(15):
    tortoisex += 5
    drawcircle()
#left leg
tortoisex = 9
tortoisey = -91
tortoiseradius = 25
for i in range(15):
    tortoisex += 6
    tortoisey += 2.7
    drawcircle()
#right leg
tortoisex = 191
tortoisey = -91
for i in range(15):
    tortoisex -= 6
    tortoisey += 2.7
    drawcircle()
#straight line again
tortoisex = 60
tortoisey = -67
tortoisradius = 15
for i in range(12):
    tortoisex += 6
    drawcircle()
#negative space near abdomen
tortoise.color(255,255,255)
tortoisex = 38
tortoisey = -23.5
tortoiseradius = 14
drawcircle()
tortoisex = 162
drawcircle()
tortoise.penup()
tortoisex = 100
tortoisey = 0
#arrow head draw
tortoisex = 94
tortoisey = 179
drawarrow()
#removal of a bit of line w a circle
tortoisex = 101
tortoisey = 185
tortoiseradius = 5
drawcircle()
#earth symbol
tortoise.penup()
tortoise.home()
tortoisex = -200
tortoisey = 65
tortoise.setposition(tortoisex,tortoisey)
tortoise.width(5)
#greenish color
tortoise.color(64,203,74)
tortoise.pendown()
#leftside backwards "E"
tortoise.forward(30)
tortoise.right(90)
tortoise.forward(12)
tortoise.right(90)
tortoise.forward(34)
tortoise.right(180)
tortoise.forward(34)
tortoise.right(90)
tortoise.forward(12)
tortoise.right(90)
tortoise.forward(46)
tortoise.right(90)
tortoise.forward(12)
#leftside angle bit 
tortoise.right(15)
tortoise.forward(80)
#top portion; in middle stop to go down to make spiral
tortoise.right(75)
tortoise.forward(30)
#spiral begin
tortoise.right(90)
tortoise.penup()
tortoise.forward(30)
tortoise.pendown()
tortoise.width(1)
tortoise.left(90)
for i in range (30):
    distanceadd = 0
    distanceadd += i/4
    tortoise.forward(distanceadd)
    tortoise.right(40)
#return back to top line
tortoise.penup()
tortoise.setheading(0)
tortoise.left(180)
tortoise.forward(12)
tortoise.right(90)
tortoise.width(5)
tortoise.forward(32)
#back to drawin da top
tortoise.pendown()
tortoise.right(90)
tortoise.forward(30)
#rightside angle bit 
tortoise.right(75)
tortoise.forward(80)
tortoise.right(15)
tortoise.forward(12)
#bottom right side "E"
tortoise.right(90)
tortoise.forward(46)
tortoise.right(90)
tortoise.forward(12)
tortoise.right(90)
tortoise.forward(34)
tortoise.right(180)
tortoise.forward(34)
tortoise.right(90)
tortoise.forward(12)
tortoise.right(90)
tortoise.forward(30)
screen.exitonclick()
