import os
import csv

filepath = os.path.join("Resources","budget_data.csv")
total = 0
differencelist = []

with open(filepath) as inputDoc:
    csvfile = csv.reader(inputDoc,delimiter = ",")
    #print(csvfile)
    csv_header = next(csvfile)
    #print("CSV Header ",csv_header)

   # No_of_rows = len(list(csvfile))
    #print("Total Months: ", No_of_rows)
    
    firstrow = next(csvfile)
    rowcount = 1
    total = total + int(firstrow[1])
    
    
    #print(firstrow)
    currentvalue = float(firstrow[1])
    #print (currentvalue)

    for row in csvfile:
        total = total + int(row[1])
        rowcount = rowcount + 1
        difference = float(row[1]) - currentvalue
        currentvalue = float(row[1])
        
       # print (difference)
       # differencelist = differencelist + [difference]
        differencelist.append(difference)   
        if (difference == max(differencelist)):
            maxProfMonth = row[0]
        
        elif (difference == min(differencelist)):
            MinProfMonth = row[0]
        

      #  print(differencelist)

  #      average(differencelist)
    changeAverage = sum(differencelist)/len(differencelist)
    GreatestIncrease = max(differencelist) 
    GreatestDecrease = min(differencelist)
    
    Financial_Analysis = (f"Financial Analysis\n-----------------------\n"
    f"Total Months: {rowcount}\n"
    f"Total: ${total}\n"
    f"Average Change:{round(changeAverage,2)}\n"
    f"Greatest Increase in Profits: {maxProfMonth} $({GreatestIncrease})\n"
    f"Greatest Decrease in Profits: {MinProfMonth} $({GreatestDecrease})")

    print(Financial_Analysis)
   # print ("Financial Analysis\n-------------------------")
   # print ("Total Months:",rowcount)
   # print ("Total: $"+str(total))
   # print ("Average Change:",round(changeAverage,2))    
    #print(maxProfMonth)  
    #print(maxProfMonth)
   # print("Greatest Increase in Profits:",maxProfMonth, "$(" + str(GreatestIncrease)+")")
   # print("Greatest Decrease in Profits:",MinProfMonth, "$(" + str(GreatestDecrease)+")")

    with open("analysis/Financial Analysis.txt","w") as textfile:
        textfile.write(Financial_Analysis)

