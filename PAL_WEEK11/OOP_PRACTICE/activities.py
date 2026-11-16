# Helper functions 
# "Activities" simulation

# Notice how you can refer to them as a person - you don't need to specify what type of person
def make_introductions(room): 
    """
    Simulates people in a room introducing themselves. 
    """
    print("Please introduce yourselves: ")
    for person in room: 
        person.introduce() 
        person.question() 
    print()

def make_observations(room): 
    """
    Simulates making observations about people in a room. 
    """
    print("Let's observe what everyone is doing: ")
    for person in room:
        person.observe() 
    print() 
