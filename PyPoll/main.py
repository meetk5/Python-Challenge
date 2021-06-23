from typing import Counter
#import pandas as pd
import os
import csv

filepath = os.path.join("Resources","election_data.csv")
rowcount = 0
candidate_list = []
new_list = []
percentlist = []
valuelist = []
index = 0


with open(filepath) as csvFile:
    csvreader = csv.reader(csvFile,delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        rowcount = rowcount + 1
        candidate_list.append(row[2])
      
    for candidate in candidate_list:
        if candidate not in new_list:
            new_list.append(candidate)

    #print(Counter(candidate_list))  
    candidate_dict = dict(Counter(candidate_list))
    #print(candidate_dict)

    winner = max(candidate_dict.values())
  #  winner_name = candidate_dict.keys().winner

    for key,value in candidate_dict.items():
        valuelist.append(value)
        percent = (int(value)/rowcount)*100
        percentlist.append(percent)
        if value == winner:
            winner_name = key

#   print(percentlist)
#   print(valuelist)
#   print(new_list)
#print(candidate_list)
election_analysis = ("\nElection Results\n"
        "\n---------------------------------\n"
        f"Total Votes:{rowcount}\n"
        "---------------------------------\n"
        f"{new_list[0]}: {round(percentlist[0],4)}% ({valuelist[0]})\n"
        f"{new_list[1]}: {round(percentlist[1],4)}% ({valuelist[1]})\n"
        f"{new_list[2]}: {round(percentlist[2],4)}% ({valuelist[2]})\n"
        f"{new_list[3]}: {round(percentlist[3],4)}% ({valuelist[3]})\n"
        "---------------------------------\n"
        f"Winner: {winner_name}\n"
        "---------------------------------\n")
print(election_analysis)

with open("analysis/Election Analysis.txt","w") as textfile:
        textfile.write(election_analysis)

