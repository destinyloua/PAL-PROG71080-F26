# PAL PROG71080
# WEEK 5

# FUNCTION REVIEW 
# Start using PEP-8 formatting 

# PEP-8: functions use lowercase_snake_casing + should be descriptve but not too long 
def add_numbers(x, y): 
    """Returns the sum of two numbers."""   # this is a PEP-8 docstring (explains what your function does)
    return x + y 

# Functions don't always "return" something, but they should always DO SOMETHING USEFUL 
def print_stuff(): 
    """Prints a string."""
    print("This function just prints stuff.")

# Not a useful funtion 
def nothing_function(): 
    """Literally does nothing."""
    pass    # can use 'pass' as a placeholder but come back and make this do something later 

# Separates functions from runnable program 
# Not 'necessary' but good practice and will be useful later 
if __name__ == "__main__": 
    # Watch your indenting now 

    # Call your function 
    sum1 = add_numbers(1, 5)
    print(f"{sum1}")

    # Do it again with a twist 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(f"{num1} + {num2} = {add_numbers(num1, num2)}")

    # Call another function 
    print_stuff()       # NOTE: you didn't promise this function anything (no input parameters), so don't give it anything 
