
# Problem 1
# month_names = ["january", "february", "march", 
# "april", "may", "june", 
# "july", "august", "september", 
# "october", "november", "december"]
# 
# month_days = ["31", "28 or 29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
# 
# from_user = input("Please enter the name of a month: ")
# month_index = 0
# for month in month_names:
#     if from_user.lower() == month:
#         print("There are", month_days[month_index], "days in", month)
#     month_index += 1


# Problem 2

# word_list = []
# 
# while True:
#     from_user = input("Please enter a word. Just press the <Enter> key to continue: ")
#     
#     if from_user == "":
#         break
#     
#     else:
#         word_list.append(from_user)
#         
# if len(word_list) == 1:
#     print(word_list[0])
#     
# else:
#     print(word_list[0], end="")
#     counter = 1
#     while counter != (len(word_list) - 1):
#         print(", " + word_list[counter], end="")
#         counter += 1
#     print(" and", word_list[counter])

# Problem 3

output_dict = {}

from_user = input("Please enter a word or phrase: ")
char_counter = 0
for char in from_user:
    if char not in output_dict:
        output_dict[char] = 1
        char_counter += 1
    else:
        output_dict[char] += 1

print("Number of unique characters:", char_counter)
print("Output dictionary:", output_dict)
        