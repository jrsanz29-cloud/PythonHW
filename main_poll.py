import os
import csv
t_vote_cast = 0
dict_candidates={}
percent_candi={}
name=''
high_count=0
high_key=''
csvpath = "/Users/josesanchez/Desktop/PythonHW/03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #print(csvreader)
    csv_header=next(csvreader)
    
    for row in csvreader:

        t_vote_cast=t_vote_cast +1
        if row[2] not in dict_candidates.keys():
            dict_candidates[row[2]]= 0
            #print(dict_candidates)
        else:
            #print(row[2])
            name=row[2]
            dict_candidates[name]=dict_candidates[name]+1

    for k,v in dict_candidates.items():
        percent_candi[k] = round((v / t_vote_cast)*100,2)

    high_count = max(dict_candidates.values())
    high_key= [ k for k, v in dict_candidates.items() if v== high_count]    
        
print("Election Results")
print("___________________________")

print(f"Total Votes: {t_vote_cast}")
print("___________________________")
for k,v in percent_candi.items():

    print(f'{k}:{percent_candi[k]}% ({dict_candidates[k]})')
print("___________________________")
print(f" Winner: {high_key[0]}")


    
