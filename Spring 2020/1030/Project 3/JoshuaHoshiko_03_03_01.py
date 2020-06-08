
# Joshua Hoshiko
# Project 3 problem 1
# A simple tempurature conversion table

# Introduction print
print("This is a temperature conversion table for between Celsius and Fahrenheit")
print("Celsius  Fahrenheit")

# Calculate the tempuratures up to 100 celsius
celsius = 0
while celsius <= 100:
    fahrenheit = (celsius * (9/5)) + 32
    print("%3d         %3d"%(celsius, fahrenheit))
    celsius += 10