#import library
import os
import csv
import statistics as stat

#joining path
pf = os.path.join('C:\\Users\\display\Desktop\PythonHW\PyBank\Resources\Budget_data.csv')
# open and read csv
with open('C:\\Users\\display\Desktop\PythonHW\PyBank\Resources\Budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")


    #set variable for profit and loss
    Profit = []
    Loss = []

    #read through each row of data after header
    for _ in csvreader:
        Profit.append(int(_[1]))
        Loss.append(_[0])

   # calculate total length of months
    totalMonths = len(Loss)
    # find revenue change
    revenueChange = []

    for _ in range(1, len(Profit)):
        revenueChange.append((int(Profit[_]) - int(Profit[_-1])))
    
        # calculate average revenue change
    #revenueAverage = sum(revenueChange) / len(revenueChange)
    revenueAverage = stat.mean(revenueChange)
        # greatest increase in revenue
    greatestIncrease = max(revenueChange)
        # greatest decrease in revenue
    greatestDecrease = min(revenueChange)
       

def printResults():
    print(f"\u0332".join("FINANCIAL ANALYSIS"))
    print(f"total months: {str(totalMonths)}\n") 
    print(f"Total: ${str(round(sum(Profit)))}\n")
    print(f"Average change: ${str(round(revenueAverage))}\n")
    print(f"Greatest Increase in Profits: {str(Loss[revenueChange.index(max(revenueChange))+1])} ${str(greatestIncrease)}\n")
    print(f"Greatest Decrease in Profits: {str(Loss[revenueChange.index(min(revenueChange))+1])} ${str(greatestDecrease)}\n")
printResults()

    
def printTextFile():
    file = open("budgetdata.txt","w")
    file.write(f"Financial Analysis\n")
    file.write(f"...................................................................................." "\n")
    file.write(f"total months: {str(totalMonths)}\n")
    file.write(f"Total: ${str(round(sum(Profit)))}\n")
    file.write(f"Average change: ${str(round(revenueAverage))}\n")
    file.write(f"Greatest Increase in Profits: {str(Loss[revenueChange.index(max(revenueChange))+1])} ${str(greatestIncrease)}\n")
    file.write(f"Greatest Decrease in Profits: {str(Loss[revenueChange.index(min(revenueChange))+1])} ${str(greatestDecrease)}\n")
    file.close()
printTextFile()