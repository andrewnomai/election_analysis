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

# Write three counties to the file.

    txt_file.write("Counties in the Election\n")
    txt_file.write("-----------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


# 1. Initialize a total vote counter.

total_votes = 0

# Candidate Options

candidate_options = []

# 1. Declare the empty dictionary
candidate_votes = {}

# Winning Candidadate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.

with open(file_to_load) as election_data:


    # To do: read and analyze the data here. 

    file_reader = csv.reader(election_data)

    # Print the header row

    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.

    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

    # Print the candidate name for each row
        candidate_name = row[2]

    # If the candidate does not match any existing candidate . . .
        if candidate_name not in candidate_options:


            # Add it to the list of candidates
            candidate_options.append(candidate_name)


            # 2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0


    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:

    # 2. Retreive vote count of a candidate

    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.

    vote_percentage = float(votes) / float(total_votes) * 100



# To do: print out each candidate's name, vote count, and percentage of # votes to the terminal.
print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')


    # Determine winning vote count and candidate 
    # Determine if the votes is greater than the winning count.
    
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then set winning_count = votes and winning_percentage =
        # votes_percentage. 

        winning_count = votes
        winning_percentage = vote_percentage

        # And, set the winning_candidate equal to the candidate's name.

        winning_candidate = candidate_name