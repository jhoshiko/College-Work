
# Joshua Hoshiko
# Project 3 problem 2

# lists for storing information
num_list = []
greater_list = []
lesser_list = []
equal_list = []

# Intordution priht
print("This program accepts a series of numbers and returns information about the numbers.")
print("Enter a '0' when you are done inputing numbers\n")

# Get the list of numbers from the user, filtering out bad entries till a '0' is entered
while True:
    from_user = input("Please enter a number: ")
    
    if not from_user.isdigit():
        print("Input must be a number and non-negative!")
    
    elif int(from_user) == 0:
        break
    
    else:
        num_list.append(int(from_user))


# IF the list is empty, exit the program
if len(num_list) == 0:
    print("No numbers in the list. Exiting...")
    exit()

# Get the average of the numbers
sum = 0
for number in num_list:
    sum += number
average = sum / len(num_list)

# Sort the numbers into their respective catagories
for number in num_list:
    if number > average:
        greater_list.append(number)
    elif number == average:
        equal_list.append(number)
    else:
        lesser_list.append(number)

# Print the information
print("\nNumbers list:", num_list)
print("Average of the numbers is:", round(average, 2))
if not len(lesser_list) == 0:
    print("Numbers less than the average:", lesser_list)
else:
    print("None of the numbers are less than the average")

if not len(lesser_list) == 0:
    print("Numbers greater than the average:", greater_list)
else:
    print("None of the numbers are greater than the average")

if not len(equal_list) == 0:
    print("Numbers equal to the average:", equal_list)
else:
    print("None of the numbers are equal to the average") 