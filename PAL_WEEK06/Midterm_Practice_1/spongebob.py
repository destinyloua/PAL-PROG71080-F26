# PAL PROG71080
# WEEK 6 
# Midterm Preparation (1)

# Feel free to modify the skeleton to your liking, but make sure you produce similar output. 

# This is your data to start (global lists): 
names = ["SpongeBob", "Patrick", "Squidward", "Sandy", "Mr. Krabs", "Plankton", "Squilliam"]
jobs = ["Fry Cook", "Unemployed", "Cashier", "Scientist", "Restaurant Owner", "Restaurant Owner", "Musician"]
is_friendly = [True, True, False, True, False, False, False]
cash = [500, 10, 200, 150, 10000, 50, 5000]

class Resident: 
    """Represents a resident in Bikini Bottom."""
    def __init__(self, name, job, friendly, cash):
        self.name = name
        self.job = job 
        self.friendly = friendly
        self.__cash = cash 

    # TODO: Create a function that returns the character's cash amount (private attribute). 
    def get_cash(self): 
        pass
    
    def print_info(self): 
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Is friendly: {self.friendly}")
        print()

def get_resident_list(): 
    """Uses the global lists to create and return a list of residents."""
    residents = [] 
    for i in range(len(names)): 
        resident = Resident(
            names[i],
            jobs[i], 
            is_friendly[i],
            cash[i] 
        )
        residents.append(resident)
    return residents

def display_residents(resident_list): 
    """Displays basic information for all residents in a list."""
    for character in resident_list: 
        character.print_info()

# TODO: Create a function that returns the character with the most cash. 
def find_richest(): 
    pass 

# TODO: Create a function that returns restauraunt owners. 
def find_restaurant_owners(): 
    pass

# TODO: Create a function that returns only unfriendly characters. 
def find_unfriendlies(): 
    pass

if __name__ == "__main__": 
    # Generating the list of Bikini Bottom residents 
    bb_residents = get_resident_list() 

    # Check to make sure data populated correctly 
    print("All Bikini Bottom Residents:")
    display_residents(bb_residents)

    # TODO: Display the richest resident's name and cash. 
    print(f"\nThe richest resident in Bikini Bottom is: ")

    # TODO: Display the name and job of characters that are restaurant owners. 
    print(f"\nThese residents are restauraunt owners: ")

    # TODO: Display all non-friendly characters' basic information. 
    print(f"\nThe following characters are NOT FRIENDLY: ")



 