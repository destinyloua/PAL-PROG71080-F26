# PAL PROG71080
# WEEK 5
# CLASSES + PEP-8 DOCUMENTATION 

# My establishment needs employees 
class Employee:                                 # PEP-8: classes are single noun + start with capital 
    def __init__(self, name, role, wage): 
        """Initializes the Employee object."""  # PEP-8: docstring 
        self.name = name 
        self.role = role
        self.__wage = wage

    def get_wage(self): 
        """Returns the employee's (private) wage."""
        return self.__wage

    def set_wage(self, new_wage): 
        """Changes an employee's wage to a new wage provided."""
        self.__wage = new_wage
        print(f"Wage changed successfully.")    # Success message is nice to have 

# Hmm...what other companies will I have to compete with in the future...?
class Company: 
    def __init__(self, name, employees):
        """Initializes the Company object."""
        self.name = name
        self.employees = employees

    def hire(self, emp): 
        """Takes an employee object and appends it to the company employee list."""
        self.employees.append(emp)
        print(f"{emp.name} was hired!")

    def fire(self, emp): 
        """Takes an employee object and removes it from the company employee list."""
        self.employees.remove(emp)
        print(f"{emp.name} was fired...")

    def show_employees(self): 
        """Prints all employees in the company."""          # Modify this or add more functions 
        print(f"{self.name} Employees:")
        for emp in self.employees: 
            print(f"{emp.name}: {emp.role}")            

        
# Create employee objects
emp1 = Employee("Destiny", "Manager", 50.00)
emp2 = Employee("Barbara", "Chef", 30.00)
emp3 = Employee("Geoff", "Server", 18.00)

# Use your employee variables to access their specific info (public attributes)
print(f"Employee 2: {emp2.name}")

# For private attributes, you have to call the "getter" 
print(f"Employee 1's wage: {emp1.get_wage()}")

# A list of employees to feed to the company 
emp_list = [emp1, emp2]

# Check employees are in the list
for emp in emp_list: 
    print(f"{emp.name}")

# Create a company object 
comp1 = Company("Destiny's Diner", emp_list)
comp1.show_employees()                 # FIX: don't "print" this, it already prints within the function 
                                            # (This was why we kept getting 'None' printed)
# Hire someone 
comp1.hire(emp3)
comp1.show_employees()

# Fire someone (sorry Geoff)
comp1.fire(emp3)
comp1.show_employees()




