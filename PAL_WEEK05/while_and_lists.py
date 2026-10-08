# PAL WEEK 5 
# WHILE LOOP 
# Revamping the diner 

# Display your menu of items/services (list version)
item1 = ["Burger", 3.50]
item2 = ["Fries", 2.50]
item3 = ["Milkshake", 2.00]

# Manually print each line - add numbers for choice options 
print("Destiny's Diner Menu")
print(f"1. {item1[0]}.........${item1[1]:.2f}")
print(f"2. {item2[0]}..........${item2[1]:.2f}")
print(f"3. {item3[0]}......${item3[1]:.2f}")
print(f"4. Done")

# Ordering - you don't know what the customer wants yet so start empty 
order = [] 

# Initiates the loop 
choice = int(input("Choose an item: "))

# WHILE LOOP: best if you don't know how many items yet 
while choice != 4:      # exit loop when user enters 4 
    if choice == 1: 
        order.append(item1)
    elif choice == 2: 
        order.append(item2)
    elif choice == 3: 
        order.append(item3)
    else: 
        print("Invalid choice")     # handle unwanted input 

    # Ask again 
    choice = int(input("Choose an item: "))

# Show order items as a LIST 
print(order)

# Show order items (name only)
# FOR LOOP: best when you know how many items (manageable amount)
# For every item in the order list, print the value at index 0 of the item (i.e. the name of the item)
for item in order: 
    print(f"{item[0]}")

# UPDATED: the 'order' is now a 2D list (a list of lists) - dictionary count doesn't work 
# How to count instead...(not ideal but this uses concepts you already know)

# 1. Start all counts at 0 
count_item1 = 0
count_item2 = 0
count_item3 = 0 

# 2. Iterate and increment 
for x in order: 
    if x[0] == item1[0]:        # compare by name of item a.k.a value at index 0 
        count_item1 += 1 
    elif x[0] == item2[0]: 
        count_item2 += 1
    elif x[0] == item3[0]: 
        count_item3 += 1 
    else: 
        print("Something went wrong")       # Unlikely but good to handle anything unexpected 

# 3. Display your counts (a.k.a. quantities)
print(f"{item1[0]} x {count_item1}")
print(f"{item2[0]} x {count_item2}")
print(f"{item3[0]} x {count_item3}")


