
# Joshua Hoshiko
# Project 4, Problem 3

# Try to open file with file names
try:
    print("Attempting to open file: 1030 Project 04 03_Files.txt...")
    file_names = open("1030 Project 04 03_Files.txt", "r")
except:
    print("Error opening file that has file names!!")
    exit()

try:
    # Clear the text file
    output_file = open("JoshuaHoshiko_03_04_03_Output.txt", "w").close()
    
    # Now prepare the text file for appending
    output_file = open("JoshuaHoshiko_03_04_03_Output.txt", "a")
    
    # Open all the files in the file name file and then append their contents to the output file
    for file_name in file_names:
        try:
            revised_name = file_name.strip('\n') + ".txt"
            print("Reading file:", revised_name)
            current_file = open(revised_name, "r")
            for line in current_file:
                output_file.write(line)
            print("Done!")
            output_file.write("\n")
        except:
            print("Error opening file:", file_name)
except:
    print("Error writing to output file!!")    
output_file.close()
current_file.close()
file_names.close()