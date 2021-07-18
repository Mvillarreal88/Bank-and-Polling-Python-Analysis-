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
    Total_months = []
    Net_pl = []
    Pl_change = []

    for rows in csvreader:
        Total_months.append(rows[0])
        Net_pl.append(int(rows[1]))

    #Calculating the average revenue changes
    for value in range(1, len(Net_pl)):
        Pl_change.append((int(Net_pl[value]) - int(Net_pl[value-1])))
    
    #Len will add all the months together
    Sum_months = len(Total_months)

    Average_PL = sum(Pl_change) / len(Pl_change)

    #largest increase in revenue
    largest_increase = max(Net_pl)
    #largest decrease in revenue
    largest_decrease = min(Net_pl)

#print data analysis 

print(["Financial Analysis"])
print(["------------------------"])
print([f"Total Months: {str(Sum_months)}"])
print([f"Net Total of Profit/Loss: $ {sum(Net_pl)}"])
print([f"Average Change:  + {str(Average_PL)}"])
print("Greatest Increase in Profits: " + str(Total_months[Pl_change.index(max(Pl_change))+1]) + " " + "$" + str(largest_increase))
print("Greatest Decrease in Profits: " + str(Total_months[Pl_change.index(min(Pl_change))+1]) + " " + "$" + str(largest_decrease))