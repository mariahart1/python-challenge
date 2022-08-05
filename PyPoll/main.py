import os
import csv

# Path to collect data from the PyPoll folder
pypoll_csv = os.path.join('..', 'Pypoll', 'Resources', 'election_data.csv')

# Lists to store data
total_votes = 0

# Open the CSV
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# Remove header
    header = next(csv_reader)

# Loop
    for row in csv_reader:

# The total number of votes cast
        total_votes = total_votes + 1

# A complete list of candidates who received votes
    

# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote


# Print
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')


# Export text file
with open('py_poll.txt', 'w') as file:
    file.write('Election Results\n')
    file.write('-------------------------\n')
    file.write(f'Total Months: {total_votes}\n')
