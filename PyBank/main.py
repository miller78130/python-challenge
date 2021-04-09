import os
import csv

# Define Pathway
budget_data = os.path.join('Resources','budget_data.csv')

# Total number of Months
with open(budget_data, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    months = len(list(reader))
    total_months = months - 1

with open(budget_data, "r") as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

date = data['Date']
profit_loss = data['Profit/Losses']

profit_loss = [float(i) for i in profit_loss]

greatest_increase = max(profit_loss)

greatest_decrease = min(profit_loss)

total_profit = 0
total_profit = sum(profit_loss)

average = total_profit / total_months

average = "${:,.2f}".format(average)
total_profit ="${:,.2f}".format(total_profit)

index_1 = profit_loss.index(greatest_increase)
mylist1 = [date[index_1],profit_loss[index_1]]

date1 = mylist1[0]
profit1 = mylist1[1]
float(profit1)
profit1 ="${:,.2f}".format(profit1)

index_2 = profit_loss.index(greatest_decrease)
mylist2 = [date[index_2],profit_loss[index_2]]

date2 = mylist2[0]
profit2 = mylist2[1]
float(profit2)
profit2 ="${:,.2f}".format(profit2)

print(f"Financial Analysis")
print (f"-------------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profit}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {date1} {profit1}")
print(f"Greatest Decrease in Profits: {date2} {profit2}")

output_path = os.path.join('output','Output.csv')
with open(output_path, 'w', newline='')as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['---------------------------------------------'])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: {total_profit}"])
    csvwriter.writerow([f"Average Change: {average}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {date1} {profit1}"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {date2} {profit2}"])