#Import pandas modules
import pandas as pd
#Create reference to CSV file
csvpath = "Resources/budget_data.csv"
#Import the CSV into a pandas DataFrame
budget_df = pd.read_csv(csvpath, low_memory=False)
budget_df
#Calculate the total number of months included in the dataset
total_months = len(budget_df.index)
print(f"There are " + str(total_months) + " total months in the dataset.")
#Calculate the net total amount of "Profit"/Losses" over the entire period'
Total = budget_df["Profit/Losses"].sum()
print(Total)
#Calculate the changes in "Profits/Losses" over the entire period
#For row in budget_df["Profit/Losses"]
#skiprows = 0


#^do the diff formula I think and then add each one to a list and then divide that list by 86 to get the thing?
#Find the average of those changes

#Find greatest increase in profits (date&amount) over entire period
#Find greatest descease in losses (date&amount) over entire period
#Print analysis to terminal
#Export a text file with the results