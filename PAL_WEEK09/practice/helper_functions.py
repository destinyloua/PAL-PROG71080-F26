# Functions to help with your project (starter code)

def display_animals(animals): 
    """Displays a list of animals available for adoption."""
    for i in range(len(animals)): 
        animal = animals[i]
        print(f"{i + 1}. {animal.name} - {animal.species} - {animal.age} years old")

def get_choice(): 
    """Asks user for input and returns their input."""
    choice = int(input("Select an animal to adopt or enter 0 to exit: "))
    return choice

def run_adoption(animals): 
    # TODO: Create a function that lets a user choose an animal(s) to adopt and returns
    # a list of adopted animals.
    adopted = [] 
    return adopted

   

