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
#Calculate the changes in "Profits/Losses" over the entire period and find their average
Profit_loss = budget_df["Profit/Losses"]


def budget_change_avg(a1):
    Changes = []
    a, b =  0, 1
    while b<len(a1):
        delta = a1[b] - a1[a]
        Changes.append(delta)
        a = a+1
        b = b+1
    Sum_of_Changes = sum(Changes)
    Average_Change = (Sum_of_Changes/len(Changes))
    return [Changes, Sum_of_Changes, Average_Change]

budget_deltas = budget_change_avg(Profit_loss)
Changes = budget_deltas[0]
Sum_of_Changes = budget_deltas[1]
Average_Change = budget_deltas[2]

Greatest_Profit = max(Changes)
print(Greatest_Profit)


#Find greatest increase in profits (date&amount) over entire period
#Find greatest descease in losses (date&amount) over entire period
#Print analysis to terminal
#Export a text file with the results\


    