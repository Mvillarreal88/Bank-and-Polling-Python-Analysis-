#Import the needed modules
import os
import csv

#Set Path
election_csvpath = os.path.join("Resources", "election_data.csv")
 
#Open the CSV
with open(election_csvpath) as ele_file:
    csvreader = csv.reader(ele_file, delimiter=",")
    
    #Skipping the header row
    header = next(csvreader)


    Total_votes = 0
    candidate_list = []
    khan_votes = 0
    li_votes = 0
    otooley_votes = 0
    correy_votes = 0

    for row in csvreader:
        Total_votes += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        elif row[2] == "Khan":
            khan_votes += 1
        
        elif row[2] == "Correy":
            correy_votes += 1
        
        elif row[2] == "Li":
            li_votes += 1

        elif row[2] == "O'Tooley":
            otooley_votes += 1


    #Calculate percentages for each candidate

    per_Khan = round(khan_votes/Total_votes * 100)
    per_li = round(li_votes/Total_votes * 100) 
    per_otooley = round(otooley_votes/Total_votes * 100)
    per_correy = round(correy_votes/Total_votes * 100)

