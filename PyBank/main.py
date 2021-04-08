import os
import csv

# Define Pathway
budget_data = os.path.join('Resources','budget_data.csv')

# Total number of Months
with open(budget_data, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    months = len(list(reader))
    total_months = months - 1

with open(budget_data, "r") as csv_file:
    calc = csv.reader(csv_file, delimiter=',')
    total = 0
    for row in csv.reader(calc):
        print (col)
        for col in row[1]:
            total += int(row[1])


    
    print(f"Financial Analysis")
    print (f"-------------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: $")

#net total of profit/losses over the entire period
#with open(budget_data, "r") as csv_file:
    #reader = csv.reader(csv_file)
    #netProfitLoss = sum()

#print(f"Net Profit/Loss: {netProfitLoss}")


