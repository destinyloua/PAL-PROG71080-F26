# Data models 
# I want to keep my classes separate from my functions 

class Resident: 
    """Represents a resident in Bikini Bottom."""
    def __init__(self, name, job, friendly, cash):
        self.name = name
        self.job = job 
        self.friendly = friendly
        self.__cash = cash 

    # TODO: Create a function that returns the character's cash amount (private attribute). 
    def get_cash(self): 
        """Returns private attribute cash."""
        return self.__cash 
    
    def print_info(self):
        """Displays Resident public attributes.""" 
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Is friendly: {self.friendly}")
        print()

        