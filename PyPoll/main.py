
import os
import csv

# Path to collect data from resources folder
election_data_csv = os.path.join("Resources","election_data.csv")

# Declare Variables
count = 0
candidatelist = []
candidate_options = []
vote_count = []
vote_percent = []


# Read in the csv file 
with open(election_data_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    # Loop through data with algorithmic calculations to produce results
    for row in csv_reader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        candidate_options.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = candidate_options[vote_count.index(winning_vote_count)]
    

# Print the results and export the data to our text file
with open("Analysis.txt", 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate_options))):
        text.write(candidate_options[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")


    