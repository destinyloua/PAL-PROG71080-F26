# PUT YOUR MAIN SOURCE CODE HERE 

# In terminal: pip install pandas (if you don't have it yet)
import pandas as pd 

# If you need to access data from your data folder...(NEED PANDAS)
file_name = "../data/some_data.csv"
data = pd.read_csv(file_name)

# Print the first few lines to check if data was loaded 
print(data.head())

# Errors? 
# In terminal: cd src + run your program 
# Still struggling? 
# Come to PAL...