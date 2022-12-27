# ---------------------------------------
# Andrew Lander                         |
# CSCI 107: Assignment 5                |
# Last Modified: October 10th, 20XX     |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2021.  |
# ---------------------------------------

# This function calculates income tax based off
# an unmarried individuals income with predetermined
# values entered. It is a nested function
# used within the process function. It follows the math
# found at this link: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets

def unmarried_individual_tax(income):
    if income <= 9950:
        income = income * .1
    elif 9950 < income <= 40525:
        income = 995 + ((income - 9950) * .12)
    elif 40525 < income <= 86375:
        income = 4664 + ((income - 40525) * .22)
    elif 86375 < income <= 164925:
        income = 14751 + ((income - 86375) * .24)
    elif 164925 < income <= 209425:
        income = 33603 + ((income - 164925) * .32)
    elif 209425 < income <= 523600:
        income = 47843 + ((income - 209425) * .35)
    else:
        income = 157804.25 + ((income - 523600) * .37) 
    return income

# ---------------------------------------

def process(income):
    print("The 2021 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():

    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()
