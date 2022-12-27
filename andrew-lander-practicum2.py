import keyword
import turtle

#question one

words = input("Enter a word: ")

if (keyword.iskeyword(words)):
    print("That is a python keyword.")
else:
    print("That is not a python keyword.")

#question two

def determine_zone(latitude):
    if(0 <= latitude < 23.5):
        return("Tropical Zone")
        latitude = "Tropical Zone"
    elif(23.5 <= latitude < 66.5):
        return("Temperate Zone")
    elif(66.5 <= latitude < 90):
        return("Polar Zone")
    else:
        return("Illegal Latitude")

for latitude in range(0,101,20):
    print("Latitude:", latitude, "Classification:", determine_zone(latitude))

#question three

lines = turtle.Turtle()

def draw_lines(length,color,leg_width,leg_number):
    rotate_angle = 360/leg_number
    lines.color(color)
    lines.width(leg_width)
    for i in range(leg_number):
        lines.right(rotate_angle)
        lines.forward(length)        
        lines.goto(0,0)
        
draw_lines(100,"black",10,1)
