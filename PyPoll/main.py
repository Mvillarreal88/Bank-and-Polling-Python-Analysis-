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
candidates = []
perc_votes = 