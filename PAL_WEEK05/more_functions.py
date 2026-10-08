# PAL PROG71080
# WEEK 5 
# MORE FUNCTIONS 

def multiply(x, y): 
    """Take 2 numbers and return the product."""        # docstring 
    return x * y

def power_of(x, y): 
    """Take x and y and return x to the power of y."""
    return x ** y

def divide(x, y): 
    """Returns the quotient of x and y."""
    return x / y 

# UPDATED 
def greater_than_100(x, y): 
    """Takes 2 values and prints if each value is greater than 100.""" 
    if x > 100: 
        print(f"{x} is greater than 100")

    if y > 100: 
        print(f"{y} is greater than 100")

def both_greater(x, y): 
    """Checks if two numbers are greater than 100 and returns true/false."""
    if x > 100 and y > 100: 
        return True 
    return False            # if not true, then must return false 

def one_greater(x, y):
    """Checks if one of two numbers is greater than 100."""
    if x > 100 or y > 100: 
        return True 
    return False 

def less_than_500(x): 
    """Takes one number and determines if it is less than 500."""
    if x < 500:
        print(f"{x} is less than 500.")
        return True
    return False
    
    
# Call your functions to make variables 
product1 = multiply(30, 55)
power1 = power_of(5, 3)
quotient1 = divide(500, 4)

# Use your new variables in functions 
print(f"Comparing {product1} and {power1}...")
greater_than_100(product1, power1)                                                  # prints statements
print(f"Both greater than 100? ---> {both_greater(product1, power1)}")              # true or false
print(f"At least one greater than 100? ---> {one_greater(product1, power1)}")       # true or false 

# Another way 
print(f"Comparing {product1} and {quotient1}")
if one_greater(product1, quotient1):        # REMEMBER: this function returns a bool (true/false)
    print(f"Both greater than 100? ---> {both_greater(product1, quotient1)}")   # if its true, then do this 
    greater_than_100(product1, quotient1)   
else: 
    print("No numbers greater than 100.")