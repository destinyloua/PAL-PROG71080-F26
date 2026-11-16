# A teacher is a Person 

import person as p 

class Teacher(p.Person): 
    """
    Represents a teacher who teaches a subject. 
    """
    def __init__(self, name, age, subject): 
        super().__init__(name, age)           # Inherit these from Person class 
        self.subject = subject 

    # Function Overriding 
    def question(self): 
        """
        Prints a question and teacher related answer. 
        """
        print("Q: What do you do for a living?")
        print("A: I am a teacher")

    # Polymorphism 
    def observe(self):
        """
        Prints a teacher specific observation.
        """
        print(f"{self.name} is planning a {self.subject} lecture.")