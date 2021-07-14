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
    totalMonths = int(len(months))
    
    
    #Total amount P/L over entire period
    totalAmt = sum(values)
    ftotalAmt = "{:,}".format(sum(values))
#     print(totalAmt)  


    #Calculate changes over entire period and add to Changes list
    for x in range(len(values)-1):
        change = values[x + 1] - values[x]
        changes.append(change) 
    
    #Calculate avg of changes
    avgChange = round(sum(changes)/len(changes),2)
    favgChange = "{:,}".format(round(sum(changes)/len(changes),2))
#     print(round(avgChange,2))
    
    
    maxChange = max(changes)
    minChange = min(changes)
    fmaxChange = "{:,}".format(max(changes))
    fminChange = "{:,}".format(min(changes))
    
    
#     print(maxChange)
#     print(minChange)
    
    #Find index of max/min values
    for x in range(len(changes)-1):
        if maxChange == changes[x]:
            maxDateIdx = int(changes.index(changes[x]))   
            
        if minChange == changes[x]:
            minDateIdx = int(changes.index(changes[x]))
            break
 
    # print(maxDateIdx)
#     print(minDateIdx)

    #Use value index to match date in months list
    profitInc = months[maxDateIdx+1]
    profitDec = months[minDateIdx+1]

    #Print Analysis
    print(f"Finacial Analysis")
    print('-' * 25)
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${ftotalAmt}")
    print(f"Average Change: ${favgChange}")
    print(f"Greatest Increase in Profits: {profitInc} (${fmaxChange})")
    print(f"Greatest Decrease in Profits: {profitDec} (${fminChange})")
    
     #Export text file of results
    cleanCsv = zip([[totalMonths , totalAmt , avgChange , profitInc , maxChange , profitDec , minChange]])

    output_path = os.path.join(".", "Analysis", "PyBank_Results.txt")
    
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        csvwriter2 = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Finacial Analysis'])
        csvwriter.writerow(['--------------------'])
        csvwriter.writerow(['Total Months: ' , totalMonths])
        csvwriter.writerow(['Total: $' , ftotalAmt])
        csvwriter.writerow(['Average Change: $', favgChange])
        csvwriter.writerow(['Greatest Increase in Profits: $', fmaxChange, profitInc])
        csvwriter.writerow(['Greatest Decrease in Profits: $', fminChange, profitDec])
        csvwriter.writerow(['--------------------'])
        csvwriter2.writerows([['Total Months','Total Profit','Average Change','Increase Month','Greatest Increase in Profits','Decrease Month','Greatest Decrease in Profits']])
        csvwriter2.writerow(cleanCsv)