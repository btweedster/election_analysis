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

# Initialize a county list and county votes dictionary
county_list = []
county_votes = {}

# Declare winning candidate variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout
largest_county = ""
largest_county_votes = 0

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

        # Get the county name from each row
        county_name = row[1]

        # Add the candidate name to the candidate options if not already there
        if candidate_name not in candidate_options:

            # Add candidate name to candidate_options
            candidate_options.append(candidate_name)

            # Add candidate name to candidate_votes
            candidate_votes[candidate_name] = 0
        
        # Add vote to candidate count
        candidate_votes[candidate_name] += 1

        # Check if county is in county list
        if county_name not in county_list:
            
            # Add county name to county list
            county_list.append(county_name)

            # Add county name ot county votes
            county_votes[county_name] = 0
        
        # Add vote to county votes
        county_votes[county_name] += 1
    
    # Save the results to txt file
with open(file_to_save,"w") as txt_file:

    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )

    # Print results and save to txt file
    print(election_results,end="")
    txt_file.write(election_results)

    # Loop through al counties and calculate and print their percentage of the vote
    for county in county_votes:

        votes = county_votes[county]

        vote_percentage = float(votes) / float(total_votes) * 100

        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print county results and save to file
        print(county_results)
        txt_file.write(county_results)

        # Determine the largest county turnout
        if votes > largest_county_votes:

            largest_county = county

            largest_county_votes = votes
    
    # Establish largest county and formatting
    county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"

    )

    # Print and save largest county with 
    print(county_summary)
    txt_file.write(county_summary)

    # Loop through all candidates and calculate and print their percentage of the vote
    for candidate_name in candidate_options:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidate results and save to file
        print(candidate_results)
        txt_file.write(candidate_results)

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

    # Print winning candidate summary and save to txt file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)