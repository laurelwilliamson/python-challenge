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
Candidates = election_df["Candidate"].unique()
print(Candidates)

#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.