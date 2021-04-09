import os
import csv

# Define Pathway
election_data = os.path.join('Resources','election_data.csv')

with open(election_data, "r") as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]
#create lists for each column
voter_id = data['Voter ID']
county = data['County']
candidate = data['Candidate']

#Get total votes
total_votes = len(voter_id)

#vote count per candidate
candidate_1_votes = candidate.count('Khan')
candidate_2_votes = candidate.count('Correy')
candidate_3_votes = candidate.count('Li')
candidate_4_votes = candidate.count("O'Tooley")

#Verify those are the only candidates listed
#candidate = list(dict.fromkeys(candidate))#
#print(candidate)

#define candidate names
candidate_1 = 'Khan'
candidate_2 = 'Correy'
candidate_3 = 'Li'
candidate_4 = "O'Tooley"

#find votes percentage
candidate_1_percentage = '{:.2%}'.format(candidate_1_votes / total_votes)
candidate_2_percentage = '{:.2%}'.format(candidate_2_votes / total_votes)
candidate_3_percentage = '{:.2%}'.format(candidate_3_votes / total_votes)
candidate_4_percentage = '{:.2%}'.format(candidate_4_votes / total_votes)

#find winner
votes_list = [candidate_1_votes, candidate_2_votes, candidate_3_votes, candidate_4_votes]
winning_votes = max(votes_list)

if candidate.count('Khan') > candidate.count('Correy') & candidate.count('Li') & candidate.count("O'Tooley"):
    winner = 'Khan'
else:
    if candidate.count('Correy') > candidate.count('Li') & candidate.count("O'Tooley"):
        winner = 'Correy'
    else: 
        if candidate.count('Li') > candidate.count('Khan') & candidate.count('Correy') & candidate.count("O'Tooley"):
            winner = 'Li'
        else:
            if candidate.count("O'Tooley") > candidate.count('Khan') & candidate.count('Li') & candidate.count('Correy'):
                winner = "O'Tooley"

print(f'Election Results')
print(f'---------------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------------')
print(f'{candidate_1} {candidate_1_percentage} ({candidate_1_votes})')
print(f'{candidate_2} {candidate_2_percentage} ({candidate_2_votes})')
print(f'{candidate_3} {candidate_3_percentage} ({candidate_3_votes})')
print(f'{candidate_4} {candidate_4_percentage} ({candidate_4_votes})')
print(f'---------------------------')
print(f'Winner: {winner}')
print(f'---------------------------')