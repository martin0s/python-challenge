#Import Dependencies
import os
import csv

#Declare file
csvpath = os.path.join("Resources", "election_data.csv")


#Declare Variables
total_votes=0
candidate_list=[]
votes={}
percentage=0
percentage_list=[]
winner_vote=0
winner=""


#Open CSV
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
        total_votes=total_votes+1
        if row[2] not in candidate_list:
        
             candidate_list.append(row[2])
             votes[row[2]]=0
        votes[row[2]]=votes[row[2]]+1
        percentage=round(((votes[row[2]])/total_votes)*100,2)
    percentage_list.append(percentage)


#Average fore each candidate
Charles_percentage=round((votes["Charles Casper Stockham"]/total_votes)*100,2)
Diana_percentage=round((votes["Diana DeGette"]/total_votes)*100,2)
Raymon_percentage=round((votes["Raymon Anthony Doane"]/total_votes)*100,2)


#Loop through candidate list to delare the winner and number of votes
for name in candidate_list:
    if votes[name]>winner_vote:
        winner_vote=votes[name]
        winner=name
print(winner,winner_vote)
    


print("Election Results")
print("------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------")
print(f"Candidate Name: {candidate_list[0]} with {votes[candidate_list[0]]} votes at {Charles_percentage}%")
print(f"Candidate Name: {candidate_list[1]} with {votes[candidate_list[1]]} votes at {Diana_percentage}%")
print(f"Candidate Name: {candidate_list[2]} with {votes[candidate_list[2]]} votes at {Raymon_percentage}%")
print(winner)

#Output Results in Textfile
output_file = ("PyPollResults.txt")

with open(output_file,"w") as file:
    
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Candidate Name: {candidate_list[0]} with {votes[candidate_list[0]]} votes at {Charles_percentage}%")
    file.write("\n")    
    file.write(f"Candidate Name: {candidate_list[1]} with {votes[candidate_list[1]]} votes at {Diana_percentage}%")
    file.write("\n")
    file.write(f"Candidate Name: {candidate_list[2]} with {votes[candidate_list[2]]} votes at {Raymon_percentage}%")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("----------------------------")
