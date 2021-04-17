import csv

print("Welcome to the budgeteer! Please choose a csv file name to import")
filename = "test.csv"
mydict = {}

with open(filename, mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

print(dict_from_csv)



# Import csv, run the math on the numbers, export to terminal
#Once that works, expand functionality
#Once that works, test with storing into database
#Once that works, test with presenting in front end
#Once that works, fucking rock it