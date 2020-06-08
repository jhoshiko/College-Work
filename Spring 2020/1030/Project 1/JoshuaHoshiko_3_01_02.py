import sys

# A simple program that converts miles per gallon to liters per kilometer
# Joshua Hoshiko

# Conversion factors
mpg_to_kpl = .425

# Intro print out
print ("This program converts miles per gallon to liters per kilometer")

# Ask user for mpg and validate that it is a number
mpg = input("Please enter how many miles per gallon you get: ")
if not mpg.isdigit() or int(mpg) < 0:
    print ("Input muust be a number and none negative! User entered: " + mpg)
    sys.exit()

# Convert the mpg to kpl
kpl = round(float(mpg) * mpg_to_kpl, 1)

# Print the result
print (str(mpg) + " miles per gallon is equivilent to: " + str(kpl) + " kilometers per liter")