# PAL PROG71080
# EXTRA FUNCTION STUFF 

def find_max(list): 
    """Returns the highest value in a list."""
    return max(list)

def find_max_manual(list): 
    """Compares every item in a list and returns the highest value."""
    max = list[0]       # set max as first value by default 
    for x in list:      # this will be SLOW if your list has a lot of items...
        if x > max:
            max = x     # reset max if a bigger number comes along 
    return max 

# TODO: use the same logic to define a function that returns minimum instead 

# SIMPLE LIST OF INTEGERS
numbers = [5, 12, 43, 1, 78, 48, 15, 1, 2, 90]
print(f"Easier Max Function: Max = {find_max(numbers)}")
print(f"Manual Max Function: Max = {find_max_manual(numbers)}")     # see output, they should be the same result 

# 2D LIST 
student_grades = [
    ["Destiny", 95], 
    ["Susan", 60], 
    ["Fred", 75], 
    ["Tyler", 40]
]

# Find student with the highest grade
top_student = max(student_grades, key = lambda x: x[1])         # this might be new to you 
print(f"The top student is {top_student[0]} who achieved {top_student[1]}%!")

# TODO: Repeat but find student with lowest grade. 

