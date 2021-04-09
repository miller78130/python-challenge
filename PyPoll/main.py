import os
import csv

# Define Pathway
election_data = os.path.join('Resources','election_data.csv')

#with open(election_data, "r") as csv_file:
    #reader = csv.reader(csv_file, delimiter=',')

#votes = len(list(reader))
#actual_votes = votes - 1

#print(f" Actual Total: {actual_votes}")
# verify pathway is correct
    #print(reader)

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

#get total votes and vote count per candidate
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


print(f'Election Results')
print(f'-------------------------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------------------------------------------------------')
print(f'{candidate_1} {candidate_1_percentage} ({candidate_1_votes})')
print(f'{candidate_2} {candidate_2_percentage} ({candidate_2_votes})')
print(f'{candidate_3} {candidate_3_percentage} ({candidate_3_votes})')
print(f'{candidate_4} {candidate_4_percentage} ({candidate_4_votes})')
print(f'-------------------------------------------------------------------------')
#print(f'{winning_candidate')
