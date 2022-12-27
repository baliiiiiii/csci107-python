# -----------------------------------------+
# Your name                                |
# CSCI 107, Assignment 7                   |
# Last Updated: Month Day, Year            |
# -----------------------------------------|
# A brief description of the assignment.   |
# -----------------------------------------+

#---------------------------------------------------------
#This function is basically the whole program. It iterates
#through a series: 1 - (1/3) + (1/5) - (1/7)... , where
#the denominator adds by two every trial and the sign is
#flipped every trial. 
#Denominator is the denominator of such series.
#Swap is a 1, used to switch between positive and negative.
#Value is the current value of the series.
#Oldvalue is the previous value, used for the variable,...
#precision, which is the absolute difference of value
#and oldvalue. 
#Difference is what it is because any value higher
#is the difference from initial (1), so no trials
#should be conducted if the precision is that high.
#Maximum trials is simply the max number of trials
#alloted by the user in case the while statement's
#condition is never satisfied. 
#---------------------------------------------------------

def leibniz_pi_estimate(precision, maximum_trials):
    denominator = int(3)
    swap = int(1)
    value = int(1)
    oldvalue = int(1)
    counter = int(1)
    difference = .44444444444
    print("Initial estimate of pi/4: 1")
    
    while(difference > precision):
        oldvalue = value
        value -= swap/denominator
        swap = swap * -1
        denominator += 2
        difference = abs(oldvalue - value)
        print(("Trial: %.0f" %(counter)) + (' Current estimate of pi/4: %.16f' %(value)))
        counter += 1
      
        if(counter > maximum_trials):
            break
    
    return value * 4
        

# -----------------------------------------

def main():
    precision = float(input("Enter desired precision for pi/4 estimate: "))
    maximum_trials = int(input("Enter the maximum number of trials: "))
    print("Final estimate of pi =", leibniz_pi_estimate(precision, maximum_trials))

# -----------------------------------------

main()
