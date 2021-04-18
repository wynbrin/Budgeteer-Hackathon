import csv
import pandas as pd
import json
import random

def reconfigure(df):
    change_e = list()
    change_reoc =list()

    for each in list(df['Reoccurring?']):
        if each == 'No':
            change_reoc.append('False')
        else:
            change_reoc.append('True')
    for each in list(df['Essential?']):
        if each == 'No':
            change_e.append('False')
        else:
            change_e.append('True')

    df['Reoccurring?'] = change_reoc
    df['Essential?'] = change_e

    return df

def group(df):
    
    df = reconfigure(df)
    group_date = list()
    group_info = list()

    for i in range(len(df)):
        info = dict()
        date = dict()
        p_id = random.randint(10000, 99999)
        
        
        date["Year"] = df['Year'][i]
        date["Month"] = df['Month'][i]
        date["Day"] = df['Day'][i]
       
        date['Purchase ID'] =p_id


        info['Purchase ID'] = p_id
        info['Income'] = df["Income"][i]
        info['Expenses'] = df["Expenses($)"][i]
        info['Description'] = df['Description'][i]
        info['Reoccurring'] = df['Reoccurring?'][i]
        info["Essential"] = df['Essential?'][i]


        group_date.append(date)
        group_info.append(info)

    return (group_date, group_info)

def make_df(filename='test.csv'):
    #filename = "test.csv"

    df = pd.read_csv(filename)

    return df

#print("Welcome to the budgeteer! Please choose a csv file name to import")


df = make_df()
grouped = group(df)

print(grouped)


    
   
