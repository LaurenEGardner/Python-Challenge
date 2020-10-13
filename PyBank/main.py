#Create script that calculates: 
    #Total number of months
    #net total amount of "profit/losses" over entire period
    #average of changes in "profit/losses"
    #greatest increase in profits (date & amount)
    #greatest decrease in losses (date & amount)

import os
import csv 

csvpath = os.path.join('Resources','budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    ##Variables
    Months = 0
    Total = 0
    Average_Change = 0
    Greatest_Increase_Amount = 0
    Greatest_Increase_Month = ""
    Greatest_Decrease_Amount = 0
    Greatest_Decrease_Month = ""
    Folder = {}

    csv_header=next(csvreader)
    print(f"CSV Header:{csv_header}")
    
    for row in csvreader:
        Months += 1
        Total += int(row[1])

        if int(row[1]) > Greatest_Increase_Amount:
            Greatest_Increase_Amount = int(row[1])
            Greatest_Increase_Month = row[0]

        if int(row[1])< Greatest_Decrease_Amount:
            Greatest_Decrease_Amount = int(row[1])
            Greatest_Decrease_Month = row[0]

    #this feels wrong but my brain wont work right now to fix it
    Average_Change = round(Total/Months)

    
    with open('output.txt', 'w') as f:
        print("Financial Analysis", file=f)
        print("----------------------------", file=f)
        print("Total Months: " + str(Months), file=f)
        print("Total: " +"$" + str(Total), file=f)
        print("Average Change: ", "$", str(Average_Change), file=f)
        print("Greatest Increase in Profits: ", Greatest_Increase_Month, "($", str(Greatest_Increase_Amount), ")", file=f)
        print("Greatest Decrease in Profits: ", Greatest_Decrease_Month, "($", str(Greatest_Decrease_Amount), ")",  file=f)
    
       
