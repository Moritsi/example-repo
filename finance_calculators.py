import math

# Finance_calculators.py
# Capstone project, the user can chose between an investment calulator
# or a bond calculator.

print("Please select which calculations you would like to do. ")
print(""" \n Investment - to calcuate interst earned.
      Bond - to calculate bond repayment. """)

# Ask user if they want to calculate their investments or bond.
user_input = input("\nChoose between investment or bond: ").lower()

# If ueser coses investment, proceede as follow
if user_input == "investment":
    print("Investment")

# Request users input on the following, inital deposit
# interest rate
# number of year on the investment
    money_deposited = float(input("Enter the amount deposited: "))
    interest_rates = float(input("Enter the annual rate: (as a percentage): "))
    number_of_years = float(input("Enter the number of years invested: "))

# Request input from user if they want to calculate simple or compound interst.
    interest = input("Do you want to calculate 'simple' or 'compound' interest: ").lower()
    if interest == "simple":
        print("Simple")

# Calculations of the simple interest
    P = float(f"{money_deposited}")
    rate = float(f"{interest_rates}")
    t = float(f"{number_of_years}")

# Convert the interest rate to percentage in decimal
    r = rate
    r = rate / 100

    if interest == "simple":
        A = P * (1 + r * t)
        print(f"If you selected simple interest, your investments will be: R{A:.2f}")

    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print(f"If you selected compound interest, your investments will be worth: R{A: 2f}")

# If bond was selected 
elif user_input == "bond":
    print("Bond")

# Request the value of the house for user
# Request the annual rate
# request the number of year to repay
    value_of_the_house = float(input("What is the value of the house: "))
    annual_interest_rate = float(input("Enter the annual interst rate: "))
    months_to_repay = float(input("How many months is the repayment plan: "))

# The bond repayment calculations.
    P = float(f"{value_of_the_house}")
    rate = float(f"{annual_interest_rate}")
    n = float(f"{months_to_repay}")

# Convesrting first the annula rate into decimals
    i = rate
    i = (rate / 100) / 12

# Calculate the bond repayment plan 
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(f"Monthly repayment is: R{repayment:2f}")
