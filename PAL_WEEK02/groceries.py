# PAL Week #2
# Thursday September 17, 2026
# Sample Solution 

# Takes the price of an item and amount of cash, then returns the difference (change)
def calculate_change(price, cash): 
    return cash - price 


if __name__ == "__main__": 
    # Prints the name of the grocery item 
    print("Double A batteries")

    # Declaring variables for easier readability 
    price = 14.99
    cash = 20.00

    # Calling the change function 
    change = calculate_change(price, cash)

    # Displaying the variables and results 
    print("Item price: ", price)
    print("Total tendered: ", cash)
    print("Change: ", change) 

    









     