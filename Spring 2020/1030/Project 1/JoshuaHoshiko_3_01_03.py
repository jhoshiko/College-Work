import sys

# A simple program finds the color of a chessboard square given coordinates
# Joshua Hoshiko

# Valid entry lists
valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
even_black = ['b', 'd', 'f', 'h']
odd_black = ['a', 'c', 'e', 'g']
valid = False

# Intro print out
print("This program finds the color of a chessboard square given coordinates")
print("Please enter a two character coordinate in the form XY,")
print("where X is a letter between A and H")
print("and where Y is a number between 1 and 8")

# Ask user for the coordinate
coordinate = input("Please enter the coordinate: ").lower()

# Check the length of the coordinate. Reject if it is not 2 characters long
if len(coordinate) != 2:
    print(str(coordinate) + " is an invalid length!")
    sys.exit()

# Check for a valid letter
for letter in valid_letters: 
    if coordinate[0] == letter:
        valid = True
        break

# Check for a valid number only if the first check passed
if valid:
    valid = False
    for number in valid_numbers:
       if coordinate[1] == number:
           valid = True
           break

# Reject the coordinate if it violates any of these checks and exit
if not valid:
    print(str(coordinate) + " is an invalid coordinate!")
    sys.exit()

# Determine the color
if int(coordinate[1]) % 2 ==0:
    color = "white"
    for letter in even_black:
        if coordinate[0] == letter:
            color = "black"
            break
    print("The color of " + str(coordinate) + " is: " + color)
    sys.exit()       
else:
    color = "white"
    for letter in odd_black:
        if coordinate[0] == letter:
            color = "black"
            break
    print("The color of " + str(coordinate) + " is: " + color)
    sys.exit()  