# -----------------------------------------+
# Andrew Lander                            |
# CSCI 107, Assignment 2                   |
# Last Updated: September 12, 2022         |  
# -----------------------------------------|
# This is an evolution of our business card|
# assignment. Instead of simply displaying |
# a business card, it gets user input and  |
# formats it accordingly.                  |  
# -----------------------------------------+

#name variables
name = input("Please enter your first name: ")
namelen = len(name)
lastname = input("Please enter your last name: ")
namelength = len(name) + len(lastname) + 2 #two because two spaces 

#phone number variables
pnumber = input("Please enter your telephone number: ")
pnumberenum = enumerate(pnumber)
pnumberarray = list(pnumberenum)
goodnumber = bool()
goodnumber0 = bool()
firstnum = int()
secondnum = int()
thirdnum = int()

#length calc variables
bcardlength = len("+------------------------------------------------+")
remainlength = (bcardlength - (namelength + 16))
remainlengthnum = (bcardlength - (namelen + 41)) #this has spaces compensated for here instead of at variable

blank = " "
blank1 = ""

"""
need to find the count of the name - the remaining length of the business card
establish this variable now, add after name + lastname (and the space!!!)
name is 16 characters past init of line
other line is static till name@email; 38 characters in
"""

"""
Okay, so this is a bit of a weird solution for this but here's my thought process:
- i need to ensure that the user a. enters only numbers in the correct location, and b. enters hyphens in the correct location
in order to meet the requirements. () doesnt matter because I can concatanate those and it's not part of the input.
- pnumber is a string by virtue of it being created from input()
- since it's a string, we can use .split (i know this from recently using it at work in PowerShell)
- it has to be 12 characters long, by virtue of requirements of the assignment. this allows for specific index location checks.
- once we have it split up, try (literally haha) to convert each array object of pnumber to an int. if we can, cool!
that means the user entered a number. otherwise, they didn't, and we can throw this under our while loop and have
the user reenter it until the bool cond clears out.

Basically:
I can establish length first, as the check for the hyphens depends on the length of the string.
After this, I can split the string up based on the position of those hyphens...
and then finally, check if those characters between the hyphens actually are integers.
"""

#initial checks: check for length first as to allow our array-specific index locations to work.
if len(pnumber) != 12:
    goodnumber = False
    #print("failed init length check")
else:
    goodnumber = True
#now check for hyphens in the proper location.
#man...are the arrays always like this? why do I have to enter the whole (index,"x") deal? tuple???
if(goodnumber):
    if pnumberarray[3] != (3,"-") or pnumberarray[7] != (7,"-"):
        goodnumber = False
        #print("failed init hyphen check")
#finally, check to see if each portion between hyphens is convertable to int. if not, it aint an int, so it aint a phone number.
#seperate bool for this one because it'll clear the while function otherwise.
if(goodnumber):
    #print(pnumber.split("-",3))
    for i in pnumber.split("-",3):
        try:
            i = int(i)
        except: 
            goodnumber0 = False
            #print("failed init int check")

while(goodnumber == False or goodnumber0 == False):
    #this is specifically a nested while because it NEEDS to be true for the other two to work. 
    while len(pnumber) != 12:
        print("It's gotta be xxx-xxx-xxxx. Try again.")
        #print("failed latter length check")
        pnumber = input()
        pnumberenum = enumerate(pnumber)
        pnumberarray = list(pnumberenum)
    else:
        goodnumber = True
    if pnumberarray[3] != (3,"-") or pnumberarray[7] != (7,"-") or len(pnumber) != 12:
        print("It's gotta be xxx-xxx-xxxx. Try again.")
        #print("failure at latter hyphen check")
        goodnumber = False
        pnumber = input()
        pnumberenum = enumerate(pnumber)
        pnumberarray = list(pnumberenum)
        
    else:
        goodnumber = True
    if(goodnumber):
    #originally if you put a wrong number in, it'd iterate through that bad number 3 times until you entered a new one.
    #this is solved by 1. setting goodnumber to false, ensuring the while loop runs again in some capacity (not sure exactly where lol).
    #2. using break to escape the for loop, but only after resetting the value of pnumber within that except.
        for i in pnumber.split("-",3):
            #print(i)
            try:
                i = int(i)
                goodnumber0 = True
                goodnumber = True
            except:
                #print(pnumber.split("-",3))
                print("It's gotta be xxx-xxx-xxxx. Try again.")
                #print("failure at latter int check")
                goodnumber0 = False
                pnumber = input()
                pnumber.split("-",3)
                pnumberenum = enumerate(pnumber)
                pnumberarray = list(pnumberenum)
                break
            

#originally I was trying to ljust on the lastname variable. ljust is TOTAL width of string, and I was trying to add
#a VARIABLE amount to a VARIABLE instead of adding that VARIABLE amount to a STATIC int.
finalnumber = str()

#simple loop to convert string to list back to string that can be concatanated after all our checks are done
for i in pnumber.split("-",3):
    finalnumber += i
#split that bad boy up so I can cocatanate the init with ()
splitnumber = 3
splitmore = 6
final, YUH = finalnumber[:splitnumber],finalnumber[splitmore:]
#lil strange once again right here but I'm tired now so I don't really care. it's nice working with very stringently set strings.
number = finalnumber.replace(final, "")
number1 = number.replace(YUH,"")
lowercasename = name.lower()

#print(finalnumber)
#print(final)
#print(number1)
#print(YUH)

line3 = ("|   -|          " + name + blank +lastname + blank.ljust(remainlength) + "|")
#print(remainlengthnum)
line10 = ("| Work: " + "(" + final + ")" + "-" + number1 + "-" + YUH + "  @: " + lowercasename + "@parasail.com" + blank1.ljust(remainlengthnum) + "|")

print("")
print("Here is your business card.")
print("")
print("+------------------------------------------------+")
print("|    |                                           |")
print(line3)
print("|  --|          Tribute Liabilities Associate    |")
print("| ---|          Parasail Capital                 |")
print("| ---------                                      |")
print("|  -------      4 Hunger Plaza                   |")
print("|               STE 1400                         |")
print("|               District 12, Panem 00012         |")
print("|                                                |")
print(line10)
print("+------------------------------------------------+")


#random links used:
#https://stackoverflow.com/questions/13838081/assigning-a-range-to-an-array-in-python question: i need to assign a range to array
#https://www.w3schools.com/python/ref_func_isinstance.asp check for int, kinda did it a different way but still used this for a minnit.
#https://stackoverflow.com/questions/58656740/python-check-if-tuple-contain-only-integers-with-while arrays are strange in python.
#https://stackoverflow.com/questions/22102685/subtract-string-text-from-string-text this was at the end, i needed to split my phone number...
#...down the middle, in two places. variables finalnumber, number, number1, and YUH come to mind.

#comment dump while I was working (remnants of code that didn't work or for debug):

#for i in pnumberarray:
#    if i[0] == "-":
#        print("its a hypen!")
    
#and i in pnumberenum != list(range(0,9))
#first check for length of pnumber

#line3varspace 
#line11var
#print(list(enumerate(pnumber)))

#print(pnumberarray[range(3,5,1)])
#print(pnumberarray[1])

#for i in pnumberarray:
#    if not(pnumberarray[i], int):
#        print("noninteger detected at " + i)

#if pnumberarray[0].isnumeric:
#    print("element 0 integer")

#print(name.center(10))
#print(namelength)
#print(bcardlength)
#print(remainlength)
