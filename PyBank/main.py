import os
import csv

months=[]
values=[]
changes=[]


csvpath = os.path.join('.', 'Resources','budget_data.csv')

with open(csvpath) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    csvheader = next(csvreader)
#     print(csvheader)


    #Enter profit/loss values into values list & months into months list
    for data in csvreader:
        values.append(int(data[1]))
        months.append(data[0])     
    totalMonths = len(months)
    
    
    #Total amount P/L over entire period
    totalAmt = "{:,}".format(sum(values))
#     print(totalAmt)  


    #Calculate changes over entire period and add to Changes list
    for x in range(len(values)-1):
        change = values[x + 1] - values[x]
        changes.append(change) 
    
    #Calculate avg of changes
    avgChange = "{:,}".format(round(sum(changes)/len(changes),2))
#     print(round(avgChange,2))
    
    
    maxChange = "{:,}".format(max(changes))
    minChange = "{:,}".format(min(changes))
    
#     print(maxChange)
#     print(minChange)
    
    #Find index of max/min values
    for x in range(len(changes)-1):
        if maxChange == changes[x]:
            maxDateIdx = int(changes.index(changes[x]))   
        
        if minChange == changes[x]:
            minDateIdx = int(changes.index(changes[x]))
    
 
    # print(maxDateIdx)
#     print(minDateIdx)

    #Use value index to match date in months list
    profitInc = months[maxDateIdx + 1]
    profitDec = months[minDateIdx + 1]

    #Print Analysis
    print(f"Finacial Analysis")
    print('-' * 25)
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalAmt}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: {profitInc} (${maxChange})")
    print(f"Greatest Decrease in Profits: {profitDec} (${minChange})")
    
    #     #Export text file of results
#     cleanCsv = zip([totalAmt])
    cleanCsv = zip([totalAmt, avgChange, profitInc, maxChange, profitDec, minChange])
    
    
    output_path = os.path.join(".", "Analysis", "PyBank_Results")
    
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Finacial Analysis'])
        csvwriter.writerows(['Total Months','Total Profit','Average Change','Increase Month','Greatest Increase in Profits','Decrease Month','Greatest Decrease in Profits'])
        csvwriter.writerow(cleanCsv)