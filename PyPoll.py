import os
import csv

# Assign .csv data file name
file_to_load = os.path.join("resources","election_results.csv")

# Assign .txt file to save analysis
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the .csv data file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the headers
    headers = next(election_data)
    print(headers)




# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
