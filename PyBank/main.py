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

    #Initialize variables that will store our data
    Total_months = 0
    Net_pl = []
    Pl_change = []

    for rows in csvreader:
        Total_months += 1
        Net_pl.append(int(rows[1]))

    #Calculating the average revenue changes
    for value in range(1, len(Net_pl)):
        Pl_change.append((int(Net_pl[value]) - int(Net_pl[value-1])))
    
    
    Avergae_PL = sum(Pl_change) / len(Pl_change)

