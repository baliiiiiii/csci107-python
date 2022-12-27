""" CSCI 107, Assignment 6: Dice Rolling Game Simulation """

# ---------------------------------------|
# Andrew Lander                          |
# CSCI 107: Assignment 6                 |
# Last Modified: October 31, 20XX        |
# ----------------------------------------
# Program that simulates dice.           |
# It creates one die and then rolls      |
# a bunch of them. It saves the total,   |
# and sums it against a winning_sum      |
# to see if it was a "win" (used to calc |
# probability).                          |
# ----------------------------------------

import random

#--------------------------------------------------------------------------------------------------   
#sorry, I had to adapt my code because I was doing some stuff very questionably. hence the global variable.
#--------------------------------------------------------------------------------------------------   

finalvalue = int()

#--------------------------------------------------------------------------------------------------   
#this is the primary function of the program, all_trials. basically, it repeatedly runs through
#the one_trial function, and it will record a success if that function returns true. 
#this success number is then used to calculate the (rough) probability of achieving 
#the winning sum. finalvalue is reset here as well.
#--------------------------------------------------------------------------------------------------   

def all_trials(number_of_trials, winning_sum, number_of_dice, sides_on_die):
    global finalvalue
    successes = int()
    
    for i in range(number_of_trials):
        finalvalue = 0
        if(one_trial(winning_sum, number_of_dice, sides_on_die)):
            successes += 1
        probability = (successes/number_of_trials * 100)
    
    #format is: %(insert variable). 1 = a, which is minimum digits present, 2 = b, which is 
    #digits displayed after decimal point (in this case we need 2). 
    
    print(('The probability of winning is %1.2f' %(probability)) + "%.")

#--------------------------------------------------------------------------------------------------   
#this is the one_trial function, and it actually rolls the dice. it takes the final value of the 
#dice (starting at 0), and adds the final value until it either exceeds or meets the winning_sum.
#--------------------------------------------------------------------------------------------------   

def one_trial(winning_sum, number_of_dice, sides_on_die):
    global finalvalue
    all_dice = roll_dice(number_of_dice, sides_on_die)
      
    while(finalvalue < winning_sum):    
        finalvalue += all_dice
        if(finalvalue == winning_sum):
            return(True)
    
    return(False)

#--------------------------------------------------------------------------------------------------   
#this is my strange roll_dice function. instead of using a nested for loop like a normal person, I
#decided the append each of the dies to an array, then iterate through that list and create a 
#total value from there. 
#--------------------------------------------------------------------------------------------------   

def roll_dice(number_of_dice, sides_on_die):
    die_array = []
    totalvalue = int()
    
    for i in range(number_of_dice):
        one_die = roll_die(sides_on_die)
        die_array.append(one_die)
        
    for i in range(len(die_array)):
        totalvalue += die_array[i]
    
    return(totalvalue)
 
#this is the roll_die function. it simply creates a random integer from 1 
#to the user-established sides_on_die,
#and only counts in integers. 
    
def roll_die(sides_on_die):
    die_value = random.randint(1,sides_on_die)
    #print("Die value: " ,die_value)
    return(die_value)


#---------------------------------------

def main():
    """ Gather inputs from user, conduct simulation """
    number_of_trials = int(input("Enter number of trials: "))
    winning_sum = int(input("Enter winning sum for dice rolls: "))
    number_of_dice = int(input("Enter number of dice to roll: "))
    sides_on_die = int(input("Enter number of sides on each die: "))
    all_trials(number_of_trials, winning_sum, number_of_dice, sides_on_die)
#---------------------------------------

main()
