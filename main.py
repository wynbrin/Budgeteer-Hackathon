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

class budgetGrouping():

    def __init__(self, filename = 'test.csv'):
        self.df = pd.read_csv(filename)
    
    def group(self):
        
        self.df = reconfigure(self.df)
        group_date = list()
        group_info = list()

        for i in range(len(self.df)):
            info = dict()
            date = dict()
            p_id = random.randint(10000, 99999)
            
            
            date["Year"] = self.df['Year'][i]
            date["Month"] = self.df['Month'][i]
            date["Day"] = self.df['Day'][i]
        
            date['Purchase ID'] =p_id


            info['Purchase ID'] = p_id
            info['Income'] = self.df["Income"][i]
            info['Expenses'] = self.df["Expenses($)"][i]
            info['Description'] = self.df['Description'][i]
            info['Reoccurring'] = self.df['Reoccurring?'][i]
            info["Essential"] = self.df['Essential?'][i]


            group_date.append(date)
            group_info.append(info)

        return (group_date, group_info)

    def reformat(self):
        
        new_date = list()
        df = reconfigure(self.df)
        for i in range(len(self.df)):
            y = str(self.df['Year'][i])
            m = str(self.df['Month'][i])
            d = str(self.df['Day'][i])

            new_date.append(y +'-'+m+'-'+d)

        
        self.df['Date'] = new_date
        del self.df['Year']
        del self.df['Month']
        del self.df['Day']
        return self.df



#print("Welcome to the budgeteer! Please choose a csv file name to import")





    
   
