# -----------------------------------------+
# Andrew Lander                            |
# CSCI 107, Assignment 8                   |
# Last Updated: November 14, 20XX          |  
# -----------------------------------------|
# This is a set of functions to recursively|
# estimate the value of e. I like to think |
# of recursion less as layers, and more as |
# setting a position within your code.     |
# This is the final version, V3.           |
# ------------------------------------------

import math

#simple global variable so it isn't reset by the function. this represents
#our estimated value of e. didn't want e_value because it's double meaning. (e = e and e = estimate)
#we start at one because then we don't have to account for that initial, no denominator
#one.

value = 1

#function for calculating a factorial of a number, eg 3! = 3 * 2 * 1. 
#I'll be honest, one of my classmates told me that this was in the instruction so
#I yoinked it without hesitation. :) however the same principle of "layers" applies here.

def factorial(num_of_terms):
    if(num_of_terms <= 1):
        return num_of_terms
    else:
        return num_of_terms * factorial(num_of_terms - 1)

#the primary function of the program. it repeatedly adds to value recursively;
#each layer represents one of the values. let's say we put in three,
#so it starts at the "third layer," adds it, and goes up "a layer." 
#It eventually hits only one term, and simply returns the value.

def estimate_e(num_of_terms, value):
    if(num_of_terms <= 1):
        return value
    else:
        value += 1/factorial(num_of_terms - 1)
        return estimate_e(num_of_terms - 1, value)

def main():
    print("This program estimates e using Newton's method")
    print("----------------------------------------------")
    num_of_terms = int(input("Enter the number of terms in the estimation: "))
    print("Newton's Estimate =", float(estimate_e(num_of_terms, value)))
    print("math.e value      =", math.e)
    
main()

#SO, I know you guys aren't going to like this much, but I wanted
#to include my previous code that helped me understand the problem. I started
#with my usual list manipulation hijinks, then moved to a much simpler for loop,
#then finally realized I needed to include recursion in the estimate_e func and rewrote it.
#Both were functional solutions.

#V2

"""
def factorial(num_of_terms):
    if(num_of_terms <= 1):
        return num_of_terms
    else:
        return num_of_terms * factorial(num_of_terms - 1) 

def estimate_e(num_of_terms):
    value = int(1)
    if(num_of_terms <= 1):
        return num_of_terms
    else:
        for i in range(2, num_of_terms + 1):
            value += 1 / factorial(i - 1)
            #print(factorial(i))
        print(value)
        return num_of_terms


num_of_terms = int(input())

estimate_e(num_of_terms)
"""

#V1

"""
def factorial(num_of_terms):
    if(num_of_terms <= 1):
        return num_of_terms
    else:
        return num_of_terms * factorial(num_of_terms - 1)
        
def estimate_e(num_of_terms):
    value = int(1)
    value_storage = []
    final_value_storage = []
    
    if(num_of_terms <= 1):
        return(num_of_terms)
    else:
        for i in range(num_of_terms):
            value_storage.append(value)
            value += 1
        value = 1
        for i in value_storage:
            final_value_storage.append(factorial(i))
        final_value_storage.pop()
        for i in final_value_storage:
            print(1 / i)
            value += float(1 / (i))
            


        #value_storage.append(factorial(num_of_terms))
        #print(value_storage)
        #for i in value_storage:
            #print("hello")
        return(value)        


num_of_terms = int(input())


print(estimate_e(num_of_terms))
"""