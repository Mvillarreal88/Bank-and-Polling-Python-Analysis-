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


    #Assighning variables
    Total_votes = 0
    candidate_list = []
    khan_votes = 0
    li_votes = 0
    otooley_votes = 0
    correy_votes = 0


    #Using If and Elif to add to variables
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


    #Using a dictionary to add names of the candidates to their total votes received

    candidate_dict = {}

    candidate_dict["Khan"] = khan_votes
    candidate_dict["Li"] = li_votes
    candidate_dict["O'Tooley"] = otooley_votes
    candidate_dict["Correy"] = correy_votes

    #Calculate percentages for each candidate

    perc_Khan = round(khan_votes/Total_votes * 100)
    perc_li = round(li_votes/Total_votes * 100) 
    perc_otooley = round(otooley_votes/Total_votes * 100)
    perc_correy = round(correy_votes/Total_votes * 100)

    Winner = max(candidate_dict, key= candidate_dict.get)

    #Printing the results of the election
    print(["Election Results"])
    print(["---------------------"])
    print(["Total Votes: " + str(Total_votes)])
    print(["---------------------"])
    print([f"Khan: {perc_Khan}% ({khan_votes})"])
    print([f"Li: {perc_li}% ({li_votes})"])
    print([f"Correy: {perc_correy}% ({correy_votes})"])
    print([f"O'Tooley: {perc_otooley}% ({otooley_votes})"])
    print(["---------------------"])
    print(["Winner: " + Winner])

#creating variable for the output file
out_file = os.path.join(".","analysis","pypoll_analysis.txt")

#opening output file
with open(out_file, "w", newline="") as analysis:
    writer = csv.writer(analysis)
    
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------"])
    writer.writerow(["Total Votes: " + str(Total_votes)])
    writer.writerow(["---------------------"])
    writer.writerow([f"Khan: {perc_Khan}% ({khan_votes})"])
    writer.writerow([f"Li: {perc_li}% ({li_votes})"])
    writer.writerow([f"Correy: {perc_correy}% ({correy_votes})"])
    writer.writerow([f"O'Tooley: {perc_otooley}% ({otooley_votes})"])
    writer.writerow(["---------------------"])
    writer.writerow(["Winner: " + Winner])