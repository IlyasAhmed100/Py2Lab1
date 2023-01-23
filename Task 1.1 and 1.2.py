# Task 1.1

# Ask User For Number of Cities
numCities = int(input("How many cities would you like to visit?"))

# Working Out Possible Paths
factorial = 1

if numCities < 0:
    print("You cannot visit a negative number of cities!")
elif numCities == 0:
    print("You have to visit atlast one city!")
else:
    for i in range (1, numCities + 1):
        factorial = factorial * i
    print("If you would like to visit", numCities, "cities, there are", factorial, "possible paths you can take to visit them all.")

# Task 1.2

# Defining Time Variables
seconds = factorial / 1000000
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
months = days / 30
years = months / 12

# Choosing Which Time Output Is Appropriate

if seconds < 60:
    print("It will take", seconds, "seconds.")
elif minutes < 60:
    print("It will take", minutes, "minutes.")
elif hours < 24:
    print("It will take", hours, "hours.")
elif days < 31:
    print("It will take", days, "days.")
elif months < 12:
    print("It will take", months, "months.")
else:
    print("It will take", years, "years.")
