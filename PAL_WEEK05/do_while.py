# PAL WEEK 5 
# WHILE LOOP VARIATION ('DO WHILE')
# Python doesn't really have a "do while" loop, but this is a variation of the traditional while loop 

# FUNCTION REVIEW: we turned the menu display into its own function 
def show_menu(item1, item2, item3): 
    print("Destiny's Diner Menu")
    print(f"1. {item1[0]}.........${item1[1]:.2f}")
    print(f"2. {item2[0]}..........${item2[1]:.2f}")
    print(f"3. {item3[0]}......${item3[1]:.2f}")
    print(f"4. Done")

# Declare the items you sell (tuple version)
item1 = ("Burger", 3.50)
item2 = ("Fries", 2.50)
item3 = ("Milkshake", 2.00)

# Call the menu function 
show_menu(item1, item2, item3)      # REMEMBER: you promised to give your menu 3 items in the function definition 

# Taking orders - start with an empty list 
order = [] 

# DO WHILE LOOP: best if you want it to run at least once 
while True: 
    choice = int(input("Choose an item: "))

    if choice == 1: 
        order.append(item1)
    elif choice == 2: 
        order.append(item2)
    elif choice == 3: 
        order.append(item3)
    elif choice == 4: 
        break                    # if you don't break, the loop goes on forever...(BAD)
    else: 
        # print "error" message but STAY in the loop 
        print("Invalid choice")  # good practice to handle invalid input from user 

# Count quantities - DICTIONARY 
# NOTE: this does not work if the menu items are LISTS 
quantities = {}             # start with empty dictionary 
for x in order: 
    if x in quantities: 
        quantities[x] += 1  # if the item is already in the quantities list, increment by 1
    else: 
        quantities[x] = 1   # if it's not there yet, then add it with quanity 1 

# Print the dictionary items 
for item, qty in quantities.items():    # uses a built-in Python function 'items()'
    print(f"{qty} x {item[0]}")         # the item name is at index 0 