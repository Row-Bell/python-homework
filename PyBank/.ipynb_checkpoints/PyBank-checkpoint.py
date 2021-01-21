#import the pandas library as pd
import pandas as pd

#read in budget data
df_budget_data = pd.read_csv("budget_data.csv")

#Calculate the total number of months included in the dataset--------------------------------------------

#The total amount of months should be the length of the index
tot_amount_of_months = len(df_budget_data["Date"])

#Calculate the net total amount of Profit/Losses over the entire period----------------------------------------

#Take the sum of the Profit/Losses column from the budget Data
tot_amount_Profit_Losses = sum(df_budget_data["Profit/Losses"])

#Calculate Change between each month and create a new column--------------------------------------------------

#Create empty liste for the changes in profit/losses list
change_in_P_L = []

#Make dataframe budget data "Profit/Losses" into a list
P_L = list(df_budget_data["Profit/Losses"])

#initialize the month
month = 1

#Iterate throught each of the months and subtract the previous month
#Add the value into our emplty change in profit/losses list
while month<len(P_L):
    change_in_P_L.append(P_L[month]-P_L[month-1])
    month += 1
    
#Change the list back into a Series
changes_Series = pd.Series(change_in_P_L)

#Calculate the average
average_change = changes_Series.mean()

#Calculate the greatest increase in profits (date and amount) over the entire period------------------------------

#Find the greates increase in profits in the Changes series
Greatest_increase_in_Profits = changes_Series.max()

#Calculate which index the greatest increase in profits corresponds to in the change series
index_of_Greatest_increase = changes_Series[changes_Series == Greatest_increase_in_Profits].index.values

#Calculate which index they will correspond to in the budget data AND grab the date of greatest increase
Date_of_Greatest_increase_in_Profits = list(df_budget_data.loc[index_of_Greatest_increase+1, "Date"])[0]

#Calcualte the greatest increase in losses (date and amount) over the entire period--------------------------------

#Find the greates increase in losses in the Changes series
Greatest_increase_in_Losses = changes_Series.min()

#Calculate which index the greatest increase in profits corresponds to in the change series
index_of_Greatest_increase = changes_Series[changes_Series == Greatest_increase_in_Losses].index.values

#Calculate which index they will correspond to in the budget data AND grab the date of greatest increase
Date_of_Greatest_increase_in_Losses = list(df_budget_data.loc[index_of_Greatest_increase+1, "Date"])[0]

#Upload File with all the results----------------------------------------------------------------------------------
PyBank_receipt = open("PyBank.txt","w+")
PyBank_receipt.write(f"Financial Analysis \n---------------------------- \nTotal Months: {tot_amount_of_months} \nTotal: ${tot_amount_Profit_Losses} \nAverage Change: ${average_change: .2f} \nGreatest Increase in Profits: {Date_of_Greatest_increase_in_Profits} ${Greatest_increase_in_Profits} \nGreatest Increase in Losses: {Date_of_Greatest_increase_in_Losses} ${Greatest_increase_in_Losses}".format())
PyBank_receipt.close()

#Print to Console-----------------------------------------------------------------------------------------------
print(f"Financial Analysis \n---------------------------- \nTotal Months: {tot_amount_of_months} \nTotal: ${tot_amount_Profit_Losses} \nAverage Change: ${average_change: .2f} \nGreatest Increase in Profits: {Date_of_Greatest_increase_in_Profits} ${Greatest_increase_in_Profits} \nGreatest Increase in Losses: {Date_of_Greatest_increase_in_Losses} ${Greatest_increase_in_Losses}")