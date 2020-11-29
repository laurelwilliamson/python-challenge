#Import pandas modules
import pandas as pd
#Create reference to CSV file
csvpath = "Resources/budget_data.csv"
#Import the CSV into a pandas DataFrame
budget_df = pd.read_csv(csvpath, low_memory=False)
#Calculate the total number of months included in the dataset
total_months = len(budget_df.index)
print(f"Total Months:  " + str(total_months))
#Calculate the net total amount of "Profit"/Losses" over the entire period'
Total = budget_df["Profit/Losses"].sum()
print(f"Total: $" + str(Total))
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


print(f"Average Change: $" + str(round(Average_Change, 2)))
Greatest_Profit = max(Changes)
Greatest_Loss = min(Changes)

indexChanges_Loss = Changes.index(Greatest_Loss)+1
indexChanges_Profit = Changes.index(Greatest_Profit)+1

date_loss = budget_df["Date"][indexChanges_Loss]
date_profit = budget_df["Date"][indexChanges_Profit]

print(f"Greatest Increase in Price: " + str(date_profit) + " ($" + str(Greatest_Profit) + ")")
print(f"Greatest Decrease in Price: " + str(date_loss) + " ($" + str(Greatest_Loss) + ")")
# new_ind = budget_df.set_index("Profit/Losses")

# ind_df = budget_df.loc[budget_df["Profit/Losses"]==Greatest_Loss]
# print(ind_df)




#Find greatest increase in profits (date&amount) over entire period
#Find greatest descease in losses (date&amount) over entire period
#Print analysis to terminal
#Export a text file with the results\


    