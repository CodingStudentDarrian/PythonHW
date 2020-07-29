import os as os
import csv
import statistics as stat

pf = os.path.join("election_data.csv")

# A list to capture the names of candidates
candidateNames = []
# A list to capture the number of votes each candidate receives
numberOfVotes = []
# A list to capture the percent of total votes each candidate garners 
percentageOfVotes = []
# A counter for the total number of votes 
totalVotes = 0

with open(pf, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        totalVotes += 1 

        if row[2] not in candidateNames:
            candidateNames.append(row[2])
            index = candidateNames.index(row[2])
            numberOfVotes.append(1)
        else:
            index = candidateNames.index(row[2])
            numberOfVotes[index] += 1
 
    # Add to percentageOfVotes list 
    for votes in numberOfVotes:
        percent = (votes/totalVotes) * 100
        percent = percent
        percent = "%.3f%%" % percent
        percentageOfVotes.append(percent)
       
    
    # Find the winning candidate
    winner = max(numberOfVotes)
    index = numberOfVotes.index(winner)
    winning_candidate = candidateNames[index]

def printElectionResults(): 
    print("Election results")
    print("--------------------------------------------------------------------------")
    print("Total votes: " + str(totalVotes))
    print("----------------------------------------------------------------------------")
    print("Khan:" + " " + str(percentageOfVotes[0]) + "%" + "("+str(numberOfVotes[0])+")")
    print("Correy:" + " " + str(percentageOfVotes[1]) + "%" + "("+str(numberOfVotes[1])+")")
    print("Li:" + " " + str(percentageOfVotes[2]) + "%" + "("+str(numberOfVotes[2])+")")
    print("O'Tooley:" + " " + str(percentageOfVotes[3]) + "%" + "("+str(numberOfVotes[3])+")")
    print("----------------------------------------------------------------------------------------")
    print("winner: " + str(winner))
printElectionResults()


def createTextFile(): 
    file = open('pypoll.txt','w')
    file.write("Election results")
    file.write("\n....................................................................................")
    file.write("\nTotal votes: " + str(totalVotes))
    file.write("\n----------------------------------------------------------------------------")
    file.write("\nKhan:" + " " + str(percentageOfVotes[0])+ "%" + "("+str(numberOfVotes[0])+")")
    file.write("\nCorrey:" + " " + str(percentageOfVotes[1]) + "%" + "("+str(numberOfVotes[1])+")")
    file.write("\nLi:" + " " + str(percentageOfVotes[2]) + "%" + "("+str(numberOfVotes[2])+")")
    file.write("\nO'Tooley:" + " " + str(percentageOfVotes[3]) + "%" + "("+str(numberOfVotes[3])+")")
    file.write("\n----------------------------------------------------------------------------------------")
    file.write("\nwinner: " + str(winner))
    file.close()
createTextFile()