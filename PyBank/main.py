#Import the needed modules
import os
import csv


#Set Path
csvpath = os.path.join("Resources", "budget_data.csv")


#Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skipping the header row
    header = next(csvreader)
    print(header)

    #Initialize variables that will store our data
    Total_months = 0
    Net_pl = []
    Pl_changes = []

    for rows in csvreader:
        Total_months += 1
        Net_pl.append(rows[1])


print(Total_months)