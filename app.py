# Real world data cleaning application 

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""
# dependencies requirement for project

import pandas as pd
import numpy as np
import time
import os
import random

data_path = 'salesdata.xlsx'
data_name = 'Jan_sale'

def data_cleaning_application(data_path, data_name):

    print("Thank you for giving the details!")
    delay_sec = random.randint(1,4) #generating the random number for delay

    print(f'please wait for {delay_sec} seconds! Checking file path')
    time.sleep(delay_sec) # delay the process


    if not os.path.exists(data_path):
        print("Incorrect file path !")
        return

    else:
        # checking the file type the user is entering
        if data_path.endswith('.csv'):
            print("Dataset Type: csv !")
            data = pd.read_csv(data_path, encoding_errors='ignore')

        elif data_path.endswith('.xlsx'):
            print("Dataset Type: excel file !")
            data = pd.read_excel(data_path)

        else:
            print("Unknown file type !")
            return 
    
    # print delay message
    delay_sec = random.randint(1,4)
    print(f'please wait for {delay_sec} seconds! Checking rows and columns of dataset')
    time.sleep(delay_sec) # delay the process
     
    # showing number of records
    print(f"Dataset contain total rowns {data.shape[0]} \nTotal columns: {data.shape[1]}")


    # start cleaning dataset
    
    # print delay message
    delay_sec = random.randint(1,4)
    print(f'please wait for {delay_sec} seconds! Checking total duplicates')
    time.sleep(delay_sec) # delay the process

    # check duplicates
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()

    print(f"Datasets has total duplicates records: {total_duplicates}")

    # print delay message
    delay_sec = random.randint(1,4)
    print(f'please wait for {delay_sec} seconds! saving total duplicate datas')
    time.sleep(delay_sec) # delay the process

    # capture duplicates and saving the duplicates in one of the file
    if total_duplicates > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)


    # deleting duplicates and keeping unique values in df variable
    df = data.drop_duplicates()


    # print delay message
    delay_sec = random.randint(1,10)
    print(f'please wait for {delay_sec} seconds! Checking for missing values')
    time.sleep(delay_sec) # delay the process

    # find missing values(blank record)
    total_missing_value = df.isnull().sum().sum()
    missing_value_colums = df.isnull().sum()
    print(f"Dataset has total missing value: {total_missing_value}")
    print(f"Dataset contain mmissing value by column:\n{missing_value_colums}")


    # Dealing with missing values( fillna, dropna)
    # print delay message
    delay_sec = random.randint(1,6)
    print(f'please wait for {delay_sec} seconds! Cleaning the dataset')
    time.sleep(delay_sec) # delay the process

    columns = df.columns
    for col in columns:
        # filling the columns which are integer and float value with mean of that column
        if df[col].dtype in (float, int):
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            # droping the rows of the column which are empty of NaN
            df.dropna(subset=col, inplace=True)

    

     # print delay message
    delay_sec = random.randint(1,5)
    print(f'please wait for {delay_sec} seconds! Exporting datasets')
    time.sleep(delay_sec) # delay the process
    # data is cleaned now
    print(f"Congrats! Dataset is cleaned ! \nNumber of rows: {df.shape[0]} Number of columns: {df.shape[1]}")


    # save the clean dataset

    df.to_csv(f'{data_name}_Cleaned_data.csv', index=None)
    print("Dataset is saved!")


if __name__ == "__main__":
    
    print("Welcome to Data Cleaning App! ")

    # ask for path and file name from user
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")

    #calling the function
    data_cleaning_application(data_path, data_name)





    
    





    
