# the data we need to retrieve
# 1. the total number of votes cast
# 2. List of candidates who received the votes
# 3. The percentage of votes each canidadate won
# 4. The total number of votes each candidate won
# 5. The winner of the eleciton based on popular vote. 

import csv

import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file

with open(file_to_save, "w") as txt_file:

# Write three copunties to the file.

    txt_file.write("Counties in the Election\n")
    txt_file.write("-----------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Open the election results and read the file.

with open(file_to_load) as election_data:


    # To do: read and analyze the data here. 

    file_reader = csv.reader(election_data)

    # Print the header row

    headers = next(file_reader)
    print(headers)