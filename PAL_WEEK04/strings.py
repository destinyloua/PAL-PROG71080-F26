# PAL PROG71080
# WEEK 04

# STRING MANIPULATION AND THINGS 
# REMEMBER: indexes start at 0 (ZERO)!!!

# SPLICE: when you only want part of a string 
date = "2026-10-01"
year = date[:4]     # prints first 4 indexes (0, 1, 2, 3)
month = date[5:7]   # prints index 5 & 6 (BUT NOT 7)
day = date[8:10]    # prints index 8 & 9 (BUT NOT 10)

print(year) 
print(month)
print(day)

# SPLIT: when you want to turn a string into a list of strings 
full_name = "George Washington"
names_split = full_name.split(" ")
print(names_split)              # prints the list of names 
first_name = names_split[0]     # prints index 0
last_name = names_split[1]      # prints index 1 
print(f"First name = {first_name}, Last name = {last_name}")
print(f"Initials = {first_name[0]}{last_name[0]}")          # prints index 0 of first and last name 

# REMOVE EXTRA SPACES AT THE BEGINNING 
str1 = "   Conestoga College"
print(f"{str1.strip()}") 

# CHANGE CASING 
# Lowercase
str2 = "I LOVE PAL SO MUCH"     
print(str2.lower())             # prints all lowercase (NOT "PERMANENT")
print("pal" in str2)            # look at output - lowercase 'pal' is not in the string 
print(str2.index("PAL"))        # but capital 'PAL' still is 

# Uppercase 
str3 = "what's up?"
str3_upper = str3.upper()       # create a new variable if you want it changed "permanently" 
print(str3_upper)
print("P" in str3_upper)

# COUNT OCCURENCES 
str4 = "omg pal is so fun omg yes woohoo omg"
omg_count = str4.count("omg")
print(f"You said 'omg' {omg_count} times")
