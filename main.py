import csv
import pandas as pd
import json

print("Welcome to the budgeteer! Please choose a csv file name to import")
filename = "test.csv"
mydict = {}

dict_from_csv = pd.read_csv(filename)
var = dict_from_csv.loc[dict_from_csv['Year'] == 2021]
print(dict_from_csv['Expenses($)'])
set(var['Income'].drop_duplicates())
# Take year, if year == 2021, separate all those rows, save as 2021.json
# We can then separate it further by month 



# formatted = json.dumps(dict_from_csv, indent=4)
# print(formatted)



# Import csv, run the math on the numbers, export to terminal
#Once that works, expand functionality
#Once that works, test with storing into database
#Once that works, test with presenting in front end
#Once that works, fucking rock it