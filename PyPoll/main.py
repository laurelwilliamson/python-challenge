#Import modules
import pandas as pd
#Create reference to CSV file
csvpath = "Resources/election_data.csv"
#Import the CSV into a pandas DataFrame
election_df = pd.read_csv(csvpath, low_memory=False)
print("Election Results")
print("-------------------------")
#The total number of votes cast
total_votes = len(election_df.index)
print(f"Total Votes: " + str(total_votes))
print("-------------------------")
#A complete list of candidates who received votes

candidates_names = election_df["Candidate"].unique()
candidates_count = election_df["Candidate"].value_counts()
candidates_percent = election_df["Candidate"].value_counts(normalize=True).mul(100).round(3).astype(str)+ '%' 

max = 0
for i in range(0,len(candidates_percent)):
    if max < candidates_count[i]:
        max = candidates_count[i]
        winner = candidates_names[i]
    print(str(candidates_names[i])+':', candidates_percent[i], '('+ str(candidates_count[i])+ ')')
print("-------------------------")
print("Winner:", winner)
print("-------------------------")



# widths = [max(map(len, col)) for col in zip(*rows)]
# for row in rows:
#     print "  ".join((val.ljust(width) for val, width in zip(row, widths)))

#indx = index.election_df["Candidate"].value_counts()
#print(indx)



#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.