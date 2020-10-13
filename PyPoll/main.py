#Create script that calculates: 
    #Total number of votes
    #complete list of candidates who received votes
    #percentage of votes each candidate won
    #winner of the election
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    ##print(csvreader)

    csv_header=next(csvreader)
    print(f"CSV Header:{csv_header}")
    

    Totalvotes = sum(1 for row in csvreader)
    print(Totalvotes)

    candidates = {}
    for row in csvreader:
        if row[2] not in candidates:
            candidates.update({row[2] : 1})
        else:
            candidates[row[2]] += 1

    print(candidates)

    #print(len(new))
    #print(candidates)     