# Main program - the one you run 

import utils as u 
FILENAME = "../data/bb_data.csv"    # If this troubles you, try removing '..'

if __name__ == "__main__": 
    # Call function to put csv data into dataframe 
    data = u.get_data(FILENAME)

    # Verify data loaded 
    print(data.head())

    # Make the list of residents using data 
    bb_residents = u.get_residents_list(data)

    # Verify Resident objects created successfully 
    u.display_residents(bb_residents)

    # Just to show you how csv reader works the same
    # data2 = u.get_data2(FILENAME)
    # bb_residents2 = u.get_residents_list2(data2)
    # u.display_residents(bb_residents2)
    # TIP: to mass comment, higlight code then ctrl + / (same thing to undo comment)
 
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

