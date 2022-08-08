import os   
import csv

poll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

complete_total_votes=0
candidates=[]
votes=0
percent_votes={}


with open(poll_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")

    header=next(csv_reader)

    for row in csv_reader: 
        complete_total_votes=complete_total_votes+1 #originally had it as total_months=...
        if row[2] not in candidates: #allows me to not count repeats
            candidates.append(row[2])
            percent_votes[row[2]]=0
        percent_votes[row[2]]=percent_votes[row[2]]+1
        
actual_percent0=percent_votes.get(candidates[0])/complete_total_votes
actual_percent1=percent_votes.get(candidates[1])/complete_total_votes
actual_percent2=percent_votes.get(candidates[2])/complete_total_votes

if actual_percent0 > actual_percent1 and actual_percent0 >actual_percent2:
    winner=candidates[0]
elif  actual_percent1 > actual_percent0 and actual_percent1 > actual_percent2:
    winner=candidates[1]
else:
    winner=candidates[2]

print(f"Total Votes: {complete_total_votes}")
print(f"List of Candidates: {candidates}")
print(f'Percent Votes: {percent_votes}')
print(f'Actual Percent: {actual_percent0}')
print(f'Actual Percent: {actual_percent1}')
print(f'Actual Percent: {actual_percent2}')
print(winner)


with open('py_poll.txt', 'w') as text:
    text.write(f'Total Votes: {complete_total_votes}\n')
    text.write(f'Candidates: {candidates}\n')
    text.write(f'Percent Votes: {percent_votes}')
    text.write(f'Actual Percent: {actual_percent0}')
    text.write(f'Blah: {actual_percent1}')
    text.write(f'Blahh: {actual_percent2}')