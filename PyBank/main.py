import os
import csv
print(os.getcwd())
budget_data = os.path.join('Resources','budget_data.csv')
# Total number of Months
with open(budget_data, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    total_months = len(list(reader))
    
    
    print(f"Total Months: {total_months}")

#net total of profit/losses over the entire period
#with open(budget_data, "r") as csv_file:
    #reader = csv.reader(csv_file)
    #netProfitLoss = sum()

#print(f"Net Profit/Loss: {netProfitLoss}")


