# Pet Adoption Main Program 

from animal import Animal
from helper_functions import run_adoption, display_animals

if __name__ == "__main__": 

    # TODO: Create a list 5 of animals 
    animals = [] 

    # This should all work if you've implemented the adoption logic correctly
    adopted = run_adoption(animals)
    print(f"\nYou adopted the following animals: ")
    display_animals(adopted)
    