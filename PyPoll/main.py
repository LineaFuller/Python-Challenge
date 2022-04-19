import os
import csv

# Path to collect data from resources folder
election_data_csv = os.path.join("Resources","election_data.csv")


# Read in the csv file 
with open(election_data_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Declare Variables 
    header = next(csv_reader)
    count = 0
    candidate_list = []
    candidate_options = []
    vote_count = []
    vote_percent = []

    # Loop through data with algorithmic calculations to produce results
    for row in csv_reader:
        # Count the total number of votes
        count = count + 1
        # Add it to the list of candidates in the running
        candidate_list.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidate_list):
        candidate_options.append(x)
        # y is the total number of votes per candidate
        y = candidate_list.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
    
    
   # Then add a vote to that candidate's count
    winning_vote_count = max(vote_count)
    winner = candidate_options[vote_count.index(winning_vote_count)]


# For each Candidate...
    for i in range(len(set(candidate_options))):
        # Print Name, Percent, and Total Vote Count
            print(candidate_options[i] + str(vote_percent[i]) + "%" + str(vote_count[i]))


# Export the results to a text file under Analysis

pypoll_file = os.path.join("Analysis", "analysis.txt")
with open(pypoll_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Total Vote: ${str(count)}\n")
    outfile.write("-------------------------\n")
    for i in range(len(set(candidate_options))):
            outfile.write(f"{candidate_options[i]}: {(round(vote_percent[i]))}%, {str(vote_count[i])} Votes\n")
    outfile.write("---------------------------------------\n")
    outfile.write(f"The winner is: {winner}\n")
    outfile.write("---------------------------------------\n")
