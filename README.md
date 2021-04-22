# Budgeteer-Hackathon
Josh Grabenstein

Sai Nayan Malladi

Wynton Britton

    Sample Files:

test - Sheet1(2).csv 

bigbigfile - myFile0(1).csv 

    main.py:

Imported packages: csv, pandas, json, random, tkinter, from tkinter import filedialog

    budgetGrouping Class:

   __init():__ initializes a budgetObject as a DataFrame converted from a csv. The filename is either retrieved through the use of a tkinter object (opens a FileExplorer window), or use the default filename argument. The sample file is test.csv.
   
   __group():__ groups the DataFrame into two lists of dictionaries and returns them as a tuple. The dictionaries correspond to the future implementation of a RDBMS and are indexed by the rows of the DataFrame. The dictionaries in the firstlist contain the date and randomly generated ID. The dictionaries in the second contain the description, income, expenses, and if the transaction was reoccurring and/or essential.
   
   __reformat():__ Reformats the year, month and day columns to a single yyyy-(m)m-(d)d column and calculates the user's current balance by substracting the sum of the income and expenses of a row from the balance of the previous row.
   
   
   
   
   
   
   
   
    testing.py:

Run this program to show a time-series visualization of the current balance from the selected file. 

Note: The format of the csv must be in some order of Year, Month, Day, Income, Expenses, Description, Reeoccuring?, and Essential?


