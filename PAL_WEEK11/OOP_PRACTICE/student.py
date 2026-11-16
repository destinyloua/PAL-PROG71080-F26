# A student is a Person 

import person as p 

class Student(p.Person): 
    """
    Represents a student studying a major at a school. 
    """
    def __init__(self, name, age, major, school): 
        super().__init__(name, age)           # Inherit these from Person class 
        self.major = major 
        self.school = school

    # Function Overriding 
    def question(self): 
        """
        Prints a question and teacher related answer. 
        """
        print("Q: What do you do for a living?")
        print("A: I am a student.")

    # Polymorphism
    def observe(self): 
        """
        Prints a student specific observation.
        """
        print(f"{self.name} is reviewing the {self.school} Academic Integrity Policy.")
