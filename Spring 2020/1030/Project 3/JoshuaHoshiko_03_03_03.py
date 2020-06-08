
# Joshua Hoshiko
# Project 3 problem 3

# Dictionary full of postal codes
codes = {
    "A": "Newfoundland",
    "B": "Nova Scotia",
    "C": "Prince Edward Island",
    "E": "New Brunswick",
    "G": "Quebec",
    "H": "Quebec",
    "J": "Quebec",
    "K": "Ontario",
    "L": "Ontario",
    "M": "Ontario",
    "N": "Ontario",
    "P": "Ontario",
    "R": "Manitoba",
    "S": "Saskatchewan",
    "T": "Alberta",
    "V": "British Coloumbia",
    "X": "Nunavut or Northwest Territories",
    "Y": "Yukon",
}

# Introductory print 
print("Please enter Canadian postal code. Canadian postal codes are 7 characters long.")
print("The first, third and fifth characters are letters, while the second, fourth and sixth characters are digits")
print("with a blank space in between the first three characters and the last three characters,")
print("such as 'T2N 1N4' or 'X0A 1B2'.")
print("Press the enter key without a code to end the program.")

# Loops program until the user enters a blank string
while True:    
    from_user = input("\nPostal code: ").upper()
    
    # If the input is a blank, then close the program
    if from_user == "":
        print("\nShtting down...")
        break
    
    # Validate that the string is length 7, the first character is a letter, and the second character is a number
    # If it isn't, then reject the code and print an error message
    elif len(from_user) == 7 and from_user[0] in codes and from_user[1].isdigit():
        
        # Check to see if the address is rural or urban and print
        if from_user[1] == "0":
            print("This address is a rural one in ", end = '')
        else:
            print("This address is an urban one in ", end = '')
        
        # Check the dictionary for is province and print
        print(codes[from_user[0]])
    else:
        print("Invalid postal code,", from_user, "entered. Please re-enter the code.")
