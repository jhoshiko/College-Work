import sys

# A simple program that converts feet/inches to meters/centimeters
# Joshua Hoshiko

# Conversion factors
inch_in_foot = 12
cm_in_meter = 100
cm_in_inch = 2.54

# Intro print out
print ("This program converts feet and inches to meters and centimeters")

# Ask user for feet and validate that it is a number
feet = input("Please enter the number of feet first: ")
if not feet.isdigit() or int(feet) < 0:
    print ("Input must be a number and not blank! User entered: " + feet)
    sys.exit()

# Ask user for inches and validate that it is a number
inches = input ("Please enter the number of inches: ")
if not inches.isdigit() or int(inches) < 0:
    print ("Input muust be a number and not blank! User entered: " + inches)
    sys.exit()

# Get total inches and check if they are tall
inches = float(inches) + (float(feet) * inch_in_foot)
if inches > 96:
    print ("Wow, you're really tall!")

# Convert the height into meters and centimeters
centimeters = inches * cm_in_inch
meters = int(centimeters // cm_in_meter)
centimeters = int(round(centimeters % cm_in_meter))

# Print the result
print ("The equivalent height is: " + str(meters) + " meter(s), " + str(centimeters) + " centimeter(s)")