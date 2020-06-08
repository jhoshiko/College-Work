
# Joshua Hoshiko
# Project 4, Problem 2

# Frequency dictionary
letter_frequency = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0
}

# Try to open the input file
try:
    print("Attempting to open file: 1030 Project 04 02_Sentences.txt...")
    input_file = open("1030 Project 04 02_Sentences.txt", "r")
except:
    print("Error opening file: 1030 Project 04 02_Sentences.txt!!")
    exit()
    
# Try to create an output file
line_number = 0
try:
    output_file = open("JoshuaHoshiko_03_04_02_Output.txt", "w")
    
    # For each line in the input file, count the letters and add them to the dictionary
    for line in input_file:
        line_number += 1
        print("Reading and analyzing line:", line_number, "\n", line)
        for letter in line:
            if letter.isalpha():
                letter_frequency[letter.upper()] += 1
    input_file.close()
    print("\nWriting to output file...")
    
    # For each letter in the dictionary, print the frequency
    for key in letter_frequency:
        output_file.write(str(key) + " " + str(letter_frequency[key]) + "\n")
    output_file.close() 
except:
    print("Error writing to output file!!")
    exit()
