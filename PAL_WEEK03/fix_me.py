# PAL PROG71080
# WEEK 03 

def add_two_numbers(a, b): 
    """Returns the sum of two numbers."""
    return a / b

def do_something(): 
    """Prints a statement."""
    print("I do something...")

def calculate_area(length, width): 
    """Multiplies length and width to return area."""
    return length * width 

def subtract_two_numbers(x, y): 
    """Returns the difference of two numbers."""
    return x - y

def calculate_total(price, tax_rate): 
    """Calculates and returns the total price after applying tax."""
    tax = price * tax_rate
    total_price = price + tax

    return total_price


if __name__ == "__main__": 
    a = 5
    b = 10 

    print("BEFORE:")
    print("a =", a)
    print("b =", b)

    # TODO: Swap the values of a and b 

    temp = a
    a = b
    b = temp 

    # Check 
    print("AFTER:")
    print("a =", a)
    print("b =", b)

    # My shopping cart
    cart = [] 

    # Shopping...
    cart.append("Eggs")
    cart.append("Bread")
    cart.append("Milk")

    # I don't want milk anymore
    cart.remove("Milk")

    # I want chocolate instead
    cart.append("Chocolate")

    # TODO: How many items are in my cart? 
    print(f"There are {len(cart)} items in my cart.")

    # TODO: Which exact items are in my cart? 
    print(f"Cart Items: {cart}")








