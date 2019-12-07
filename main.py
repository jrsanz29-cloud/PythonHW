import os
import csv

tmonth=0
net_profit=0
net_loss=0
date_list=[]
value_list=[]

csvpath= "/Users/josesanchez/Desktop/PythonHW/03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv"

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader= next(csvreader)
    for row in csvreader:
        date_list.append(row[0])
        value_list.append(int(row[1]))
        tmonth = 1+tmonth
        if int(row[1])<0:
            net_loss = net_loss + int(row[1])
        elif int(row[1])>=0:
            net_profit = net_profit +int(row[1])
        
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Month: {tmonth}")
    print(f"Total net loss {net_loss}")
    print(f"Total profit {net_profit}")
    print(f"Grand Total {sum(value_list)}")
    print(f"Average change  {round(sum(value_list)/len(value_list))}")
    print(f"Greatest Increase in Profits: {date_list[value_list.index(max(value_list))]}  {max(value_list)}")
    print(f"Greatest Increase in Profits: {date_list[value_list.index(min(value_list))]}  {min(value_list)}")

