# Election Analysis

## Overview of Election Audit
The purpose of this project is to audit and report election results for a local congressional election in the State of Colorado. The Python script will automatically load the election data and save the results (shown below) to [election_analysis.txt](analysis/election_analysis.txt).

## Resources
- Data Source: [election_results.csv](resources/election_results.csv)
- Script: [PyPoll_Challenge.py](PyPoll_Challenge.py)
- Software: Python 3.9.6, Visual Studio Code 1.72.2

## Election Results
The following are the results of the election:

- A total of 369,711 votes were cast
- The counties in the election with their percentage of total votes and number of votes were:
    - Jefferson County residents cast 10.5% of votes with 38,855 votes.
    - Denver County residents cast 82.8% of votes with 306,055 votes.
    - Arapahoe County residents cast 6.7% of votes with 24,801 votes.
- Denver County had the largest county turnout.
- The candidates for election were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The results of for each candidate were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana Degette who received 73.8% of the vote and 272,892 votes.

## Election Audit Summary
While this script functioned well for this election audit, it can function for any future audit as well (provided the data is identically formatted in a CSV file). However, presently the script is set to open a specified data file and output file. Two changes can be made: one to allow the user to specify the data file, and one that allows the user to name the output file. This will allow the user to use any given data file without renaming it `election_results.csv` in the script, and it will allow the user to run the script without overwriting the output file for a different set of data.

1. We will change line 5 to the following two lines of code:

```
user_data_file = input("Please specify the path to and the name of the data source. > ")
file_to_load = os.path.join(user_data_file)
```

2. Similarly we will change line 8 to the following three lines of code:

```
print("WARNING! Please use a unique file name or other files will be overwritten!)
user_output_file("Please specify the path to and the name of the output file. > ")
file_to_save = os.path.join(user_output_file)
```