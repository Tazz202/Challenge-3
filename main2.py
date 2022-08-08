import os
import csv

bank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv") #thought I had to put the actual path in. Spent a long time on this. 
#also took me a long time to realize I needed to put the lists as variables. Pandas is so much more intuitive.
total_months=0
net_total=0
p_loss=0
increase=0
decrease=0
date=[]
change=[]
changed_row=[]

with open(bank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")

    header=next(csv_reader)
#at this point i spent a long time looking for and at examples. Make variables that are lists. To create list loop through the rows and append the values to the list/variable.
    for row in csv_reader: #because we don't have a df, we need to create a big list using the loop with appending each loop.
        total_months=total_months+1
        net_total=net_total + int(row[1])

        p_loss=p_loss + int(row[1]) #Tin Phat helped me with this
        date.append(row[0]) #add the value/row in the date column
        change.append(int(row[1])) #update the change in the profit/loss column

    for L in range(1, len(change)): #helped me with this too
        changed_row.append(change[1] - change[L-1])
        average_change=round(sum(changed_row) / len(changed_row),2)

        increase=max(changed_row)
        increase_month=str(date[changed_row.index(increase)])

        decrease=min(changed_row)
        decrease_month=str(date[changed_row.index(decrease)])

print('PyBank')
print(f"Total Months: {total_months}")
print(f'Total: {net_total}')
print(f'Average Change in Profit/Loss: {average_change}')
print(f'Greatest Profit Increase: {increase_month} {increase}')
print(f'Greatest Profit Loss: {decrease_month} {decrease}')


with open('py_bank.txt', 'w') as text:
    text.write(f'Total Months: {total_months}\n')
    text.write(f'Total: {net_total}\n')
    text.write(f'Average Change in Profit/Loss: {average_change}')
    text.write(f'Greatest Profit Increase: {increase_month} {increase}')
    text.write(f'Greatest Profit Loss: {decrease_month} {decrease}')