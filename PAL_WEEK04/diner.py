# PAL PROG71080
# WEEK 04

if __name__ == "__main__": 
    # 1. Display your menu of items/services. 
    burger = 3.50 
    fries = 2.50
    milkshake = 2.00 

    print("Destiny's Diner Menu")
    print(f"Burger........${burger:.2f}")
    print(f"Fries.........${fries:.2f}")
    print(f"Milkshake.....${milkshake:.2f}")
    print("------------------------------------")

    # 2. Your first customer 
    name = input("Customer name: ")
    print("------------------------------------")
    print(f"Order for: {name}")
    print("------------------------------------")

    # 3. Order one of each item and display the receipt 
    order = burger + fries + milkshake
    tax = order * 0.13
    total = order + tax # + tip_amount

    print(f"Order subtotal: ${order:.2f}")
    print(f"Tax: ${tax:.2f}")
    # 4. Ask for tip 
    print(f"Total Due: ${total:.2f}")
    print("------------------------------------")

    # TODO: Pay with cash and calculate change (hard coded)
    cash = 20.00
    change = cash - total 

    print(f"Cash: ${cash:.2f}")
    print(f"Change: ${change:.2f}")






