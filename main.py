import csv
import pandas as pd
import json
import random

def reconfigure(df):
    change_e = list()
    change_reoc =list()

    for each in list(reoc):
        if each == 'No':
            change_reoc.append('False')
        else:
            change_reoc.append('True')
    for each in list(essential):
        if each == 'No':
            change_e.append('False')
        else:
            change_e.append('True')

    df['Reoccurring?'] = change_reoc
    df['Essential?'] = change_e

    return df

def group(df):
    
    
    group_date = list()
    group_info = list()

    for i in range(len(df)):
        info = dict()
        date = dict()
        p_id = random.randint(10000, 99999)
        
        date["Year"] = year[i]
        date["Month"] = month[i]
        date["Day"] = day[i]
       
        date['Purchase ID'] =p_id


        info['Purchase ID'] = p_id
        info['Income'] = income[i]
        info['Expenses'] = expenses[i]
        info['Description'] = desc[i]
        info['Reoccurring'] = df['Reoccurring?'][i]
        info["Essential"] = df['Essential?'][i]


        group_date.append(date)
        group_info.append(info)

    return (group_date, group_info)


print("Welcome to the budgeteer! Please choose a csv file name to import")
filename = "test.csv"
mydict = {}

dict_from_csv = pd.read_csv(filename)

year = list(dict_from_csv['Year'])
month = list(dict_from_csv['Month'])
day = list(dict_from_csv['Day'])

income = list(dict_from_csv['Income'])
expenses = list(dict_from_csv['Expenses($)'])
desc = list(dict_from_csv['Description'])
reoc = list(dict_from_csv['Reoccurring?'])
essential = list(dict_from_csv['Essential?'])



# Take year, if year == 2021, separate all those rows, save as 2021.json
# We can then separate it further by month 



# formatted = json.dumps(dict_from_csv, indent=4)
# print(formatted)



# Import csv, run the math on the numbers, export to terminal
#Once that works, expand functionality
#Once that works, test with storing into database
#Once that works, test with presenting in front end
#Once that works, fucking rock it




finance = reconfigure(dict_from_csv)
grouped = group(finance)

print(grouped)


    
   
