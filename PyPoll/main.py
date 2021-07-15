import os
import csv

voters = []
candidateOptions = []
candidateDict = {}

csvpath = os.path.join('.', 'Resources','election_data.csv')

def percentages(candidate):
    name = str(candidate)
    votes = int(candidateDict[candidate])
    fVotes = "{:,}".format(votes)
    percentVote = "{:.3%}".format(votes/totalVoters)
    print(f"{name}: {percentVote} ({fVotes})")

def percentagesExp(candidate): 
    name = str(candidate)
    votes = int(candidateDict[candidate])
    fVotes = "{:,}".format(votes)
    percentVote = "{:.3%}".format(votes/totalVoters)
    return(f"{name}: {percentVote} ({fVotes})")
    
    
with open(csvpath) as voterfile:
    csvreader = csv.reader(voterfile, delimiter=',')
    csvheader = next(csvreader)  
#     print(csvheader)
#     for row in csvreader:
#         print(row)

    #Data reader and assignments
    for data in csvreader:
        voters.append(int(data[0]))
        candidateVotes = data[2]
        #Create candidate dictionary and counts
        ##Count section modified from professor Drews code
        if candidateVotes not in candidateOptions:    
            candidateOptions.append(candidateVotes)
            candidateDict[candidateVotes] = 0
        candidateDict[candidateVotes] += 1
#     print(candidateOptions)
#     print(candidateDict)
#     print(candidateOptions)
    
          
    #Total Voter Calculation
    totalVoters = int(len(voters))
    ftotalVoters = "{:,}".format(len(voters))
#     print(totalVoters)
#     print(ftotalVoters)
    
    # Determine the winner
    for key in candidateOptions:
        if candidateDict[key] == max(candidateDict.values()):
            winner = key
#     print(winner)    
    
    
    # Print out election results
    print(f'Election Results')
    print('-'*27)
    print(f'Total Votes:  {ftotalVoters}')
    print('-'*27)
    for row in candidateOptions:
        percentages(row)
    print('-'*27)
    print(f'Winner:  {winner}')
    print('-'*27)

        
    
    #Exporting Results
    output_path = os.path.join(".", "Analysis", "PyPoll_Results.txt")
    
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        csvwriter.writerow([f'Election Results'])
        csvwriter.writerow(['-------------------------------'] )
        csvwriter.writerow([f'Total Votes:  {ftotalVoters}'])
        csvwriter.writerow(['-------------------------------'])
        for row in candidateOptions:
            csvwriter.writerow([percentagesExp(row)])
        csvwriter.writerow(['-------------------------------'])
        csvwriter.writerow([f'Winner:  {winner}'])
        csvwriter.writerow(['-------------------------------'])