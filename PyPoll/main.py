#Terrence Cummings
#03-Python Honework
#PyPoll exercise

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
#Initialize counter and tracker variables to null
    num_votes = 0
    num_counties = 0
    num_candidates = 0
# candidate list in form [[candidate name, % vote, vote count]]
    candidate_list = []
    
#list of votes in form [[voter ID, county, candidate]]
    vote_list = []

#for each vote
    for row in csvreader:
#add current month's data to the vote list
        vote_list.append(row)
#read the current month's data from the list
        vote = vote_list[num_votes]
        voter_ID = vote[0]
        county = vote[1]
        vote_for = vote[2]
        if (vote_for not in candidate_list):
            candidate_list.append(vote_for)
#            candidate_list(str(vote_for).index(2)) = candidate_list(vote_for.index(2)) + 1
        num_votes = num_votes+1
    print(num_votes)
    print(candidate_list)


#print table to terminal
#    print("Financial Analysis")
#    print("---------------------------------")
#    print("Total Months: "+str(num_months))
#    print("Total: $"+str(total_profit))
#    avg_change = tot_m_to_m_change/(num_months-1)
#    print("Average Change: $"'{:.2f}'.format(avg_change))
#    print("Greatest Increase in Profits: "+max_incr_month+" ($"+str(max_incr)+")")
#    print("Greatest Decrease in Profits: "+max_decr_month+" ($"+str(max_decr)+")")

#
#print table to text file PyBank.txt
#    f= open("PyBank.txt","w+")
#    f.write("Financial Analysis \r\n")
#    f.write("--------------------------------- \r\n")
#    f.write("Total Months: "+str(num_months)+"\r\n")
#    f.write("Total: $"+str(total_profit)+"\r\n")
#    f.write("Average Change: $"'{:.2f}'.format(avg_change)+"\r\n")
#    f.write("Greatest Increase in Profits: "+max_incr_month+" ($"+str(max_incr)+") \r\n")
#    f.write("Greatest Decrease in Profits: "+max_decr_month+" ($"+str(max_decr)+") \r\n")
#    f.close()

    