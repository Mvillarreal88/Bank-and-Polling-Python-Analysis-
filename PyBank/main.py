#Import the needed modules
import os
import csv


#Set Path
csvpath = os.path.join("Resources", "budget_data.csv")
 
#Initialize variables that will store our data
Total_months = []
Net_pl = []
Pl_changes = []




    #Open the CSV
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Skipping the header row
    header = next(csvreader)

    for row in csvreader:













#print analysis
print(["Financial Analysis"])
print(["------------------------"])
print([f"Total Months: {len(Total_months)}"])
print([f"Net Total of Profit/Loss: ${sum(Net_pl)}"])
print([f"Average Change: ${Pl_changes}"
print([f"Greatest Increase in Profits: {} (${})"])
print([f"Greatest Decrease in Profits: {} (${})"])