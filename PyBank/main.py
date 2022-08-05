import os
import csv

# Path to collect data from the PyBank folder
pybank_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Lists to store data
total_months = 0
net = 0

# Open the CSV
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# Remove header
    header = next(csv_reader)

# Loop
    for row in csv_reader:

# The total number of months included in the dataset
        total_months = total_months + 1

# The net total amount of "Profit/Losses" over the entire period
        net += int(row[1])

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

    
# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in profits (date and amount) over the entire period


# Print
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net}')
print(f'Average Change: ')
print(f'Greatest Increase in Profits: ')
print(f'Greatest Decrease in Profits: ')

# Export file
with open('py_bank.txt', 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${net}\n')
    file.write(f'Average Change: \n')
    file.write(f'Greatest Increase in Profits:\n')
    file.write(f'Greatest Decrease in Profits: \n')
