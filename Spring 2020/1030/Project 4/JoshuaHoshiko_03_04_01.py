
# Joshua Hoshiko
# Project 4, Problem 1

# Point value dictionary
point_values = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
}

# Try to open file
try:
    file = open("1030 Project 04 01 Words.txt", "r")
except:
    print("Error opening file!!")
    exit()
total_points = 0

# For each word in the file, check each of its letters and caculate point values
for line in file:
    word_points = 0
    print("The word:", line, "is worth", end=" ")
    if len(line) < 10 or len(line) > 0:
        for letter in line:
            if letter.isalpha():
                word_points += point_values[letter.upper()]
    total_points += word_points
    print(word_points, "points\n")             

print("\nTotal points:", total_points)

file.close()   