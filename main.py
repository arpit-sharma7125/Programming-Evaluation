# ----------- QUESTION 1 -----------

# Printing my name, Arpit
print("""
\t _____  ____   ____ ____  ______ 
\t/     |     \\ |    \\    ||      |
\t|  o  ||  D  )|  o  )  | |      |
\t|     ||    / |   _/|  | |_|  |_|
\t|  _  ||    \\ |  |  |  |   |  |  
\t|  |  ||  .  \\|  |  |  |   |  |  
\t|__|__||__|\\_||__| |____|  |__|  

""")


# ----------- QUESTION 2 -----------

import math 

# Asking user for the three sides of the triangle
a = float(input("\nEnter the first side, a: "))
b = float(input("\nEnter the second side, b: "))
c = float(input("\nEnter the third side, c: "))

# calculating s
s = (a + b + c) / 2

# Calculating the area of the triangle
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Printing the area of the triangle
print("\nthe area of the triangle is:", round(area, 2))



# ----------- QUESTION 3 -----------

import random

# setting total % as 100
totalPercentage = 100

# asking for the total budget
totalBudget = int(input("\nEnter your budget: "))

# generating random percentages (realstic) 
rent = random.randint(40,50)
clothing = random.randint(10, 15)
food = random.randint(18, 25)

entertainment = totalPercentage - (rent + clothing + food)

# calculating the dollar amounts
rentbudget = round(totalBudget * (rent/100),2)
clothingBudget = round(totalBudget * (clothing/100),2)
foodBudget = round(totalBudget * (food/100),2)
entertainmentBuget = round(totalBudget * (entertainment/100),2)

# printing percentages and dollar amounts
print("\nRent \t\t\t", rent, "%\t$", rentbudget, "\nClothing \t\t", clothing, "%\t$", clothingBudget, "\nFood \t\t\t", food, "%\t$", foodBudget, "\nEntertainment \t", entertainment, "%\t$", entertainmentBuget)
