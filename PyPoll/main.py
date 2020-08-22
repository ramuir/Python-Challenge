import os
import csv 

khan = 0
correy = 0
li = 0
otooley = 0

candidate_votes = []
votes = []

winning_candidate = ""
winning_count = 0
total_votes = 0

csvpath = os.path.join('..//..','PYTHON-CHALLENGE','PyPoll','Resources','election_data.csv')

with open(csvpath,'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        candidate_votes.append(row[2])
        votes.append(row[0])
        
        
candidates_dict = {}
for key in candidates_votes:
    for value in votes:
        candidates_dict[key] = value
        votes.remove(value)
        break
    

        
        

        

        
            
        


        


        