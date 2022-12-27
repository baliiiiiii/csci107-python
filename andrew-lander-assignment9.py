# -----------------------------------------+
# Andrew Lander                            |
# CSCI 107, Assignment 9                   |
# Last Updated: December 4, 20XX           |  
# -----------------------------------------|
# This is a program to play a hangman-esque|
# game. It generates a random word from a  |
# list of canidates, and performs a variety|
# of tests on guesses for what the word may|
# be.                                      |
# -----------------------------------------|

import random

#the pokemon listed are starters in pokemon mystery dungeon: explorers of time and darkness
#i always tried to get meowth in the initial personaility test of the game
#but i'd always get skitty instead
# :)

def generate_word():
    candidates = ["pikachu", "eevee", "charmander", "bulbasaur", "squirtle", "meowth", "chikorita", "cyndaquil", "totodile", "treecko", "torchic", "mudkip", "skitty", "turtwig", "chimchar", "piplup", "munchlax"]
    return random.choice(candidates)
    
#This is the only function of the program. If I were to rewrite this,
#I would definitely break it up into some smaller pieces (functions). We'll
#go through it in pieces anyway.

def play_game(generate_word, errors_allowed):

#The initial variables. Errors tracks failed guesses. Guess becomes input() later on.
#Plays keeps track of overall plays. It could be replaced by a conditional in this code (I think).
#Reveal is a line of asterisks, and reveal_list is an array of each individual character.
#Guesslist is a list of guesses. It is appended to at the end.

    errors = int(1)
    guess = str()
    plays = int()
    reveal = "*" * len(generate_word)
    reveal_list = list(reveal)
    word = generate_word
    guesslist = []
    
    print("The word you are trying to guess has " + str(len(word))  + " letters.")
    print("An * means that you haven't yet guessed that letter.")
    
#The primary loop of the function. Everything revolves around the input() stopping the loop.
    
    while(errors <= errors_allowed):

#The very initial check of the function. If reveal (our line of asterisks) is converted
#to not have any, then the game is won. Lengthcheck is always set to false as to
#guarantee the entrance of the upcoming while loop.

        asteriskcheck = reveal.find("*")
        lengthcheck = False
        
        if(asteriskcheck == -1):
            print("Congratulations! You figured out the answer: " + word)
            break

#The "final" check of the function is set to always be true unless triggered otherwise.

        finalcheck = bool(True)
      
#This loop ensures that the character entered is one long and not a blankspace of some variety. It must be
#initialized this way as to prevent problems with checking values of the index of the word later on.    
      
        while(lengthcheck == False):
            print("Here is what is known: " + reveal)
            guess = input("Enter a letter: ")
            guess = guess.lower()

    
            if(len(guess) == 1 and guess != None and guess != "" and guess != " "):
                lengthcheck = True
            elif errors < 6:
                print("Sorry - that does not give you any new information.")
                print("You have " + str(errors_allowed - errors) + " errors left.")
                errors += 1
                print("")
            else:
                print("Sorry - that does not give you any new information.")
                print("You have " + str(errors_allowed - errors) + " errors left.")
                print("")
                print("Sorry, you lost!  The answer was " + word)
                finalcheck = False
                break   

#This has to do with the final else statement of the previous block. It exits the
#program entirely when the errors have exceeded what they should be.
        
        if(finalcheck == False):
            break
         
#Another set of resetting variables is set here. Found and dupe
#serve the same purpose - trying to create a variable that will
#error out with certain inputs. Count exists because the value of i in the
#loop that contains it is characters, not numbers.
        
        found = str()
        dupe = str()
        count = int(0)

#A check for duplicates. Index() will error out if it is not found,
#and it will suceed upon finding the first instance - exactly
#what's needed in the context of this program. It only happens
#after one object (item) has been appended to guesslist.

        if(plays >= 1):
            try:
                dupe = guesslist.index(guess)
                finalcheck = False
                print("Sorry - that does not give you any new information.")
                print("You have " + str(errors_allowed - errors) + " errors left.")
                print("")
                errors += 1
            except:
                finalcheck = True
        
#The same principle is applied here. However, this is the only point a usual index
#method of checking for characters is used, since reveal's list of 
#asterisks needs to be filled in with the correct guesses (requiring array
#positions to be used). Duplicates are not appended to guesslist due to the prior 
#function, preventing problems with the for loop finding duplicate characters in the 
#array more than once. Reveal is reset and recreated by joining the list.

        if(finalcheck):
            try:
                found = generate_word.index(guess)
                reveal = ""
                for i in word:
                    if(guess == i and len(guess) == 1):
                        reveal_list[count] = guess
                    reveal += reveal_list[count]
                    count += 1
                print("Good job - that letter was not previously known!")
            except:
                print("Sorry - that does not give you any new information.")
                print("You have " + str(errors_allowed - errors) + " errors left.")

                errors += 1                                
            guesslist.append(guess)
            print("")
        plays += 1


def main():
    print("Welcome to the CSCI 107 word challenge!")
    print("Try to guess the secret word with 6 or fewer errors.")
    print("Good luck!")
    print("----------------------------------------------------")
    errors_allowed = 6
    play_game(generate_word(), errors_allowed)

   
main()