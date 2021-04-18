import csv
import pandas as pd
import json
import random
from tkinter import *
from tkinter import filedialog
  


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
        self.df = pd.read_csv(filename).fillna(0)
    
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
        expense = list()
        df = reconfigure(self.df)
        total_asset = 0
        total = list()
        for i in range(len(self.df)):
            
            y = str(self.df['Year'][i])
            m = str(self.df['Month'][i])
            d = str(self.df['Day'][i])

            new_date.append(y +'-'+m+'-'+d)


            expense.append(-(float(self.df['Expenses($)'][i])))
            
        
        self.df['Date'] = new_date
        self.df['Expenses'] = expense
       
        del self.df['Year']
        del self.df['Month']
        del self.df['Day']
        del self.df['Expenses($)']
        for i in range(len(self.df)):
            if i == 0:

                g = self.df['Income'][i].replace(',', '')
                total_asset = float(g) + float(expense[i])

                total.append(total_asset)
            else:
                g = self.df['Income'][i].replace(',', '')
                total_asset = total[i-1] + (float(g) + float(expense[i]))
                total.append(total_asset)
        self.df["Current Total"] = total
        return self.df

    

        
    # Function for opening the
    # file explorer window
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                        ("all files",
                                                            "*.*")))
        
        # Change label contents
        label_file_explorer.configure(text="File Opened: "+filename)
        
        
                                                                                                    
    # Create the root window
    window = Tk()
    
    # Set window title
    window.title('File Explorer')
    
    # Set window size
    window.geometry("500x500")
    
    #Set window background color
    window.config(background = "white")
    
    # Create a File Explorer label
    label_file_explorer = Label(window,
                                text = "File Explorer using Tkinter",
                                width = 100, height = 4,
                                fg = "blue")
    
        
    button_explore = Button(window,
                            text = "Browse Files",
                            command = browseFiles)
    
    button_exit = Button(window,
                        text = "Exit",
                        command = exit)
    
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1)
    
    button_explore.grid(column = 1, row = 2)
    
    button_exit.grid(column = 1,row = 3)
    
    # Let the window wait for any events
    window.mainloop()

#print("Welcome to the budgeteer! Please choose a csv file name to import")





    
   
