#Question 1
firstname = input("Enter your first name: ")
age = input("Enter your age: ")
year = input("Enter a year in the future: ")
ageint = int(age)

for i in range(int(year) - 2022):
    ageint += 1

print(firstname + " - you will be " + str(ageint) + " in " + year)

#Question 2
import turtle
tortoise = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
radius = int()
tortoise.speed(0)
radius = 300
screen.screensize(600,600)
#begin circle
tortoise.setposition(0,-300)
tortoise.begin_fill()
tortoise.circle(300)
tortoise.end_fill()
#begin line 
tortoise.penup()
tortoise.setposition(-200,-200)
tortoise.width(15)
tortoise.color(255,255,255)
tortoise.left(90)
tortoise.pendown()
tortoise.forward(400)
tortoise.right(90)
tortoise.forward(400)
tortoise.right(90)
tortoise.forward(400)
tortoise.right(90)
tortoise.forward(400)
screen.exitonclick()
