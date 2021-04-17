import csv
import pandas as pd
import json

print("Welcome to the budgeteer! Please choose a csv file name to import")
filename = "test.csv"
mydict = {}

dict_from_csv = pd.read_csv(filename)
year = list(dict_from_csv['Year'])
month = list(dict_from_csv['Month'])
day = list(dict_from_csv['Day'])

income = list(dict_from_csv['Income'])
expenses = list(dict_from_csv['Expenses ($)'])
desc = list(dict_from_csv['Description'])
reoc = list(dict_from_csv['Reoccurring?'])
essential = list(dict_from_csv['Essential?'])

reconfigure(dict_from_csv)

# Take year, if year == 2021, separate all those rows, save as 2021.json
# We can then separate it further by month 



# formatted = json.dumps(dict_from_csv, indent=4)
# print(formatted)



# Import csv, run the math on the numbers, export to terminal
#Once that works, expand functionality
#Once that works, test with storing into database
#Once that works, test with presenting in front end
#Once that works, fucking rock it


def reconfigure():
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
    df['Essential?'] =change_e



    

    
   
