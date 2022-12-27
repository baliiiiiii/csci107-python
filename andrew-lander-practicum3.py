
#this was rough! I could've definitely done better,
#especially on the last question. A little more foresight
#and I would've done well.


"""
#question 1
name = input("Enter your first name: ")
firstday = input("Enter the day of your last December final: ")
secondday = input("Enter the day of your first January class: ")
vacationtime = int(firstday) + int(secondday)
print("Enjoy " + str(vacationtime) + " days of vacation " + name + "!")
"""


"""
#question 2

base = int(input())

def recursive_exponentiate(base, number):

    if(number == 0):
        return base
    else:
        base = base ** number
        return recursive_exponentiate(base, number - 1)
    


for number in range(5):
    print(3, "**", number, "=", recursive_exponentiate(3, number))
"""

"""
#question 3 

word = input()
vowels = str("aeiou")

def latinize(word):
    counter = 0
    wordlist = []
    
    for i in word:
        wordlist.append(i)
        
    for v in vowels:
        counter += 1
        for i in wordlist:
            if(v == i):
                wordlist[counter] = "ay"
            print(wordlist)

            
latinize(word)
"""

"""
#question 4 

import turtle


def draw_square(tree, tree_color, width):
    tree.color("black", tree_color)
    tree.begin_fill()
    
    for i in range(4):
        tree.forward(width)
        tree.right(90)
    
    tree.end_fill()

def draw_tree(tree, xcor, ycor, length, rows):
    swap1 = True
    swap2 = True
    color = str("red")
    
    initsquares = 1
    tree.penup()
    tree.setposition(xcor,ycor)
    tree.pendown()
    draw_square(tree, color, length)
    tree.penup()
    for i in range(rows):
            
        if(initsquares == 1):
            ycor -= 20
        xcor -= 10
        tree.setposition(xcor,ycor)
        tree.pendown()
        if(initsquares == 1):
            draw_square(tree, color, length)
        else:
            for i in range(initsquares):
                tree.penup()
                xcor += 20
                tree.setposition(xcor, ycor)
                tree.pendown()
                swap1 = not(swap1)

                draw_square(tree, color, length)
            ycor -= 20
        tree.penup()

            
        initsquares += 1


    
    
def main():
    tree = turtle.Turtle()
    tree.hideturtle()
    tree.speed(0) 
    
    draw_tree(tree, -10, 200, 20, 7)
    input()

main()
"""