# Main program - this is the one you run 

# Import your other modules  
import utils as u         # I like to give it an alias so I don't have to write 'utils.' every time 

# This is your data to start (global lists): 
names = ["SpongeBob", "Patrick", "Squidward", "Sandy", "Mr. Krabs", "Plankton", "Squilliam"]
jobs = ["Fry Cook", "Unemployed", "Cashier", "Scientist", "Restaurant Owner", "Restaurant Owner", "Musician"]
is_friendly = [True, True, False, True, False, False, False]
cash = [500, 10, 200, 150, 10000, 50, 5000]

if __name__ == "__main__": 
    # Functions are not on the main file anymore - we have to import them from utils.py so use 'u.' 
    bb_residents = u.get_resident_list(names, jobs, is_friendly, cash)

    # Verify data was loaded into the list 
    u.display_residents(bb_residents)

    # TODO: Display the richest resident's name and cash. 
    richest_resident = u.find_richest(bb_residents)             # 'u.' because the function is in utils.py !!!
    print(f"\nThe richest resident in Bikini Bottom is:")
    print(f"{richest_resident.name} with ${richest_resident.get_cash()}") 

    # TODO: Display the name and job of characters that are restaurant owners. 
    print(f"\nThese residents are restauraunt owners: ")
    restaurant_owners = u.find_restaurant_owners(bb_residents)
    for resident in restaurant_owners: 
        # Customized information: just name and job 
        print(f"{resident.name}: {resident.job}")               

    # TODO: Display all non-friendly characters' basic information. 
    print(f"\nThe following characters are NOT FRIENDLY: ")
    unfriendlies = u.find_unfriendlies(bb_residents)
    u.display_residents(unfriendlies)

    # RANKED LIST: lowest to highest cash 
    cash_ranked_asc = u.rank_cash_asc(bb_residents)
    print("Least to Most Cash:")
    for resident in cash_ranked_asc: 
        print(f"{resident.name}: ${resident.get_cash()}") 
    print()

    # RANKED LIST: highest to lowest cash 
    cash_ranked_desc = u.rank_cash_desc(bb_residents)
    print("Most to Least Cash:")
    for resident in cash_ranked_desc: 
        print(f"{resident.name}: ${resident.get_cash()}") 
    print() 

    # JOB COUNTS: list method 
    job_counts_list = u.get_job_counts(bb_residents)
    print(f"{job_counts_list}")         # You can print this nicer with formatting + indexing 

    # JOB COUNTS: dictionary method 
    job_counts_dict = u.get_job_counts_dict(bb_residents)
    print(f"{job_counts_dict}")         # You can also print this nicer 