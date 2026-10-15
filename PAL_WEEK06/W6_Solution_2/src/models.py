# Data models 

class Resident: 
    """Represents a resident in Bikini Bottom."""
    def __init__(self, name, job, friendly, cash):
        self.name = name
        self.job = job 
        self.friendly = friendly
        self.__cash = cash 

    def get_cash(self): 
        return self.__cash

    def print_info(self): 
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Is friendly: {self.friendly}")
        print()
