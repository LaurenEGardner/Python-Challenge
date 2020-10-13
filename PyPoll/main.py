##Majority of code skeleton was done with Cas's help during office hours

import os
import csv

#import csv file
election_data = os.path.join("Resources", "election_data.csv")

#declare variables
vote_count=[]
Totalvotes = 0
candidates = {}

with open (election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    #Totalvotes = sum(1 for row in csvreader)
    Winning_candidate = ""
    Highest_votes = 0

    for row in csvreader:
        Totalvotes += 1

        if candidates.get(row[2]):
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
        
    
for candidate_name, candidate_votes in candidates.items():
    #print(candidate_name, candidate_votes)
    #print(candidate_name, (candidate_votes/float(Totalvotes))*100)

    if candidate_votes > Highest_votes:
        Winning_candidate = candidate_name
        Highest_votes = candidate_votes
#print(Winning_candidate)

with open('output.txt', 'w') as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes: " + str(Totalvotes), file=f)
    print("-------------------------", file=f)
    for candidate_name, candidate_votes in candidates.items():
        print(candidate_name, ":", "{:.0%}".format((candidate_votes/float(Totalvotes))), "(", candidate_votes, ")" , file=f)
    print("-------------------------", file=f)
    print("Winner: " + str(Winning_candidate),file=f )
    print("-------------------------", file=f)