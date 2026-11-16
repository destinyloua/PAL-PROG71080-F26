# PAL WEEK 11 
# INHERITANCE 

# This is the parent class a.k.a. the blueprint or the default
class Person: 
    """
    Represents a person. 
    """
    def __init__(self, name, age): 
        """
        Creates a Person object.
        """
        self.name = name 
        self.age = age 

    def enter(self, room): 
        """
        Mimics a Person entering a room by appending them to a list.
        """
        print(f"Welcome {self.name}!")
        room.append(self)

    def introduce(self): 
        """
        Prints a basic introduction to a person. 
        """
        print(f"\nMy name is {self.name} and I am {self.age} years old.")

    def question(self): 
        """
        Prints a default question and answer. 
        """
        print("Q: What do you do for a living?")
        print("A: Live...")

    def observe(self): 
        """
        Simulates observing what a person is doing. 
        """
        print(f"{self.name} is doing absolutely nothing.")

    def exit(self, room): 
        """
        Simulates a person exiting a room. 
        """
        print(f"{self.name} left.")
        room.remove(self)
