import os
import csv

# Assign .csv data file name
file_to_load = os.path.join("resources","election_results.csv")

# Assign .txt file to save analysis
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize total vote counter, candidate options, and candidate votes
total_votes = 0
candidate_options = []
candidate_votes = {}

# Declare winning candidate variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the .csv data file
with open(file_to_load) as election_data:

    # Read csv file
    file_reader = csv.reader(election_data)

    # Read the headers
    headers = next(election_data)

    # Loop over the rows of election data
    for row in file_reader:

        # Increment the total votes count
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate options if not already there
        if candidate_name not in candidate_options:

            # Add candidate name to candidate_options
            candidate_options.append(candidate_name)

            # Add candidate name to candidate_votes
            candidate_votes[candidate_name] = 0
        
        # Add vote to candidate count
        candidate_votes[candidate_name] += 1
    
    # Loop through all candidates and calculate and print their percentage of the vote
    for candidate_name in candidate_options:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine the winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )

    print(winning_candidate_summary)