#Import Dependencies
import os
import csv

#Declare Variable
csvpath = os.path.join("Resources", "budget_data.csv")

#Declare variables
total_months=0
total_amount=0
change_in_profits=[]
best_month=""
worst_month=""
greatest_increase=["",0]
greatest_decrease=["",999999]
net_change_list=[]

#Open CSV File
with open(csvpath) as csvfile:


    #Store contents of csvfile
    csvreader = csv.reader(csvfile, delimiter=",")

    #Header Labels
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    first_row=next(csvreader)
    previous_net=int(first_row[1])

    #Loop rows through file
    for row in csvreader:

        #Calculate Total Months
        total_months = total_months + 1

        #Calculate Total Ammount of Profit
        total_amount += int(row[1])

        #The Net Change
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        net_change_list=net_change_list+[net_change]

        #Find Greatest increase and greatest decrease in profits
        if net_change>greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change
        if net_change< greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change


#Calculate Average
average=sum(net_change_list)/len(net_change_list)
    

#Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})")

#Output Results in Textfile
output_file = ("PyBankResults.txt")

with open(output_file,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")    
    file.write(f"Total: ${total_amount}")
    file.write("\n")
    file.write(f"Average Change: {average}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {best_month} (${greatest_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {best_month} (${greatest_decrease})")







