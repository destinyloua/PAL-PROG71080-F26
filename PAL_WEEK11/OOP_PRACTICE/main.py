# OOP: INHERITANCE PRACTICE

import person as p      # The parent class
import teacher as t     # A child class
import student as s     # Another child class 
import activities as a  # Helper functions 

# TODO: Create another child of the Person class and incorporate them into the main program. 

if __name__ == "__main__": 
    # Person creations
    p1 = p.Person("Alice", 21)
    t1 = t.Teacher("Bob", 53, "Python")
    t2 = t.Teacher("Claire", 36, "Math")
    s1 = s.Student("Doug", 23, "Data Analytics", "Conestoga College")

    # Simulates people entering a room 
    room = []
    p1.enter(room)
    t1.enter(room)
    t2.enter(room)
    s1.enter(room)

    # Simulates activities  
    a.make_introductions(room)
    a.make_observations(room)

    # Simulates people exiting a room 
    p1.exit(room)
    t1.exit(room)

    # Show people still in the room 
    names = [person.name for person in room]    # List comprehension 
    print(f"\nPeople remaining: {names}")

    