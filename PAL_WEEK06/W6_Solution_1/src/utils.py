# Helper functions 
# In a separate file so that main isn't too cluttered. 
# You can have more than one file like this, just make sure you import them in main as needed. 

# Import other things you used from other files in the src folder 
import models as m      # models.py has my class definitions 

# NOTE: we declared the lists in main, so you need to pass the lists to this function 
#       when you call it now! 
def get_resident_list(names, jobs, is_friendly, cash): 
    """Uses the global lists (from main) to create and return a list of residents."""
    residents = [] 
    for i in range(len(names)): 
        resident = m.Resident(
            names[i],
            jobs[i], 
            is_friendly[i],
            cash[i] 
        )
        residents.append(resident)
    return residents

def display_residents(resident_list): 
    """Displays basic information for all residents in a list."""
    for resident in resident_list: 
        resident.print_info()

# TODO: Create a function that returns the character with the most cash. 
def find_richest(resident_list): 
    """Finds and returns the resident with the most cash from a list of residents."""
    richest = resident_list[0]
    for resident in resident_list:  
        if resident.get_cash() > richest.get_cash():    # cash is a private attribute so use the getter function
            richest = resident 

    return richest 

# TODO: Create a function that returns restauraunt owners. 
def find_restaurant_owners(resident_list): 
    """Returns a list of residents that own restarunts."""

    # Option 1: for loop and if 
    # restaurant_owners = [] 
    # for resident in resident_list: 
    #     if resident.job == "Restaurant Owner": 
    #         restaurant_owners.append(resident)                        # This appends the whole resident object

    # Option 2: with map() and filter() 
    restaurant_owners = list(                                           # I want a list...        
        map(
            lambda resident: resident,                                  # of Resident objects...
            filter(
                lambda resident: resident.job == "Restaurant Owner",    # where this is true...
                resident_list                                           # from this list.
            )
        )
    )
    return restaurant_owners

# TODO: Create a function that returns only unfriendly characters. 
def find_unfriendlies(resident_list): 
    """Returns a list of residents who are unfriendly."""
    # Using map() and filter () -- but you can also use for loop and if 
    unfriendlies = list(
        map(
            lambda resident: resident, 
            filter(
                lambda resident: resident.friendly == False, 
                resident_list
            )
        )
    )
    return unfriendlies

# RANKING 
def rank_cash_asc(resident_list): 
    """Returns a list of residents ranked lowest to highest cash (ascending order)."""
    temp_list = resident_list.copy()    # COPY THE LIST so we don't ruin the original (better safe than sorry)
    ranked_list = [] 

    # Keep going UNTIL nothing left in temp list
    while len(temp_list) != 0: 
        poorest = temp_list[0]

        # You could (should) turn this part into its own function, but I will leave it like this so you 
        # can follow the logic (see function below for alternative)
        for resident in temp_list: 
            if resident.get_cash() < poorest.get_cash(): 
                poorest = resident

        # Add the new poorest to the ranked list 
        ranked_list.append(poorest)

        # Get rid of the poorest for the next iteration 
        temp_list.remove(poorest)

    # Only return the ranked list (poorest to richest)
    return ranked_list 

# BONUS: let's try DESCENDING (highest to lowest) cash 
def rank_cash_desc(resident_list): 
    """Returns a list of residents ranked highest to lowest cash (descending order)."""
    temp_list = resident_list.copy() 
    ranked_list = [] 

    while len(temp_list) != 0:
        richest = find_richest(temp_list)       # LOOK!!! You already made a function that finds richest!!!
        ranked_list.append(richest)             # Works just like the function for asc
        temp_list.remove(richest)

    return ranked_list

# COUNTING 
# Using just lists 
def get_job_counts(resident_list): 
    """Returns a 2D list of jobs with the number of residents with each job."""
    jobs = [] 
    job_counts = [] 

    # Extract all the jobs present in the list 
    for resident in resident_list: 
        job = resident.job
        
        # Add it to your list of jobs 
        if job not in jobs: 
            jobs.append(job)

    # Now go through all jobs in your list of jobs 
    for job in jobs: 
        count = 0   # Start counting at 0 

        # Go through all residents and if the job matches, increment the count by 1
        for resident in resident_list: 
            if resident.job == job: 
                count += 1

        # Now add the "mini list" to the "big list" 
        job_counts.append([job, count])

    # This returns a list of smaller lists ([job, count])
    return job_counts

# Faster - with dictionary (use with caution if your prof didn't teach this yet.)
def get_job_counts_dict(resident_list): 
    """Returns a dictionary of jobs and number of residents with each job."""
    job_counts = {}
    for resident in resident_list: 
        job = resident.job
        if job not in job_counts: 
            job_counts[job] = 1
        else: 
            job_counts[job] += 1

    return job_counts