import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)

    dates = []
    profit = []

    print("Financial Analysis")

    print("------------------------")

    for row in csvreader:
        dates.append(row[0])
        profit.append(int(row[1]))

    total_months = len(dates)
    total_profit = int(sum(profit))
    average_change = round(total_profit / total_months, 2)
    greatest_increase = int(max(profit))
    greatest_decrease = int(min(profit))

    greatest_index= profit.index(greatest_increase)
    date_increase = dates[greatest_index]
    least_index = profit.index(greatest_decrease)
    date_decrease = dates[least_index]


print(f"Total Months: {total_months}")
print(f"Total Profit: {total_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase: {date_increase} ({greatest_increase})")#am i suppose to get dates aligned with this 
print(f"Greatest Decrease: {date_decrease} ({greatest_decrease})")#?


txtpath = os.path.join('Analysis','financial_analysis.txt')

with open(txtpath, 'w') as txtfile:
    txtfile.write("    Financial Analysis" + "\n")
    txtfile.write("-----------------------------------" +"\n")
    txtfile.write("    Total Months: " + str(total_months) + "\n")
    txtfile.write("    Total Profti: " + "$" + str(total_profit) + "\n")
    txtfile.write("    Average Change: " + "$" + str(average_change) + "\n")
    txtfile.write("    Greatest Increase: " + date_increase + " $" + str(greatest_increase) + "\n")#do i need to add dates by greatest increase index and then index that of dates list?
    txtfile.write("    Greatest Decrease: " + date_decrease + " $" + str(greatest_decrease) + "\n")
    txtfile.write("-----------------------------------")






       


    


 