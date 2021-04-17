import csv
import pandas as pd
import json

print("Welcome to the budgeteer! Please choose a csv file name to import")
filename = "test.csv"
mydict = {}

dict_from_csv = pd.read_csv(filename, header=None, index_col=0, squeeze=True)
print(dict_from_csv)
# formatted = json.dumps(dict_from_csv, indent=4)
# print(formatted)



# Import csv, run the math on the numbers, export to terminal
#Once that works, expand functionality
#Once that works, test with storing into database
#Once that works, test with presenting in front end
#Once that works, fucking rock it