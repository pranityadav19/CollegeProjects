# Author: Pranit Yadav
# Program Description: This program calculates yearly retirement savings growth
# using fixed annual savings, a user-defined interest rate, and a retirement timeline.


# Prompt for annual savings; ensure it's a positive number
annualSavings = float(input("What is your annual savings amount? "))
while annualSavings <= 0:
    print("Please make sure to enter a positive number!")
    annualSavings = float(input("Enter your annual savings: "))

# Prompt for start year; must be between 2020 and 2100
startYear = int(input("What year do you want to start saving? "))
while startYear < 2020 or startYear > 2100:
    print("Please enter a start date between 2019 and 2101!")
    startYear = int(input("What year do you want to start saving? "))

# Prompt for end year; must be after start year and within allowed range
endYear = int(input("What year do you want to stop saving? "))
while endYear < 2020 or endYear > 2100 or endYear < startYear:
    print("Please enter an end date after your start date and between 2019 and 2101!")
    endYear = int(input("What year do you want to stop saving? "))

# Prompt for retirement year; must be >= end year and in range
retirementYear = int(input("What year do you want to retire?: "))
while retirementYear < 2020 or retirementYear > 2100 or retirementYear < endYear:
    print("Please enter a retirement date either the same year, higher than your end date, and between 2019 and 2101!")
    retirementYear = int(input("What year do you want to retire?: "))

# Prompt for interest rate (1–15%) and convert to decimal format
rateInput = float(input("What is the interest rate?: "))
while rateInput < 1 or rateInput > 15:
    print("please enter an interest rate between 1 and 15!")
    rateInput = float(input("What is the interest rate?: "))
interestRate = rateInput / 100  # Convert to decimal
total = 0              # Running total of retirement account balance

# Print formatted column headers with field width
print('')
print("%-6s %12s %12s %15s" % ("Year", "Savings", "Interest", "Total"))
print("-" * 50)

# Loop from startYear to retirementYear (inclusive)
for year in range(startYear, retirementYear + 1):
    if year > endYear:
        annualSavings = 0  # No more contributions after endYear
    interest = (total + annualSavings) * interestRate  # Interest earned this year
    total = total + annualSavings + interest            # Update total balance
    print("%-6d %12.d %12.d %15.d" % (year, round(annualSavings, 0), round(interest, 0), round(total, 0)))  # Print row with proper formatting
