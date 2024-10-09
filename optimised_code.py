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

import pandas as pd
import numpy as np
import time
import random
import os

# checking file is exist or not
def check_file_exist(data_file):
    if not os.path.exists(data_file):
        print("file does not exist!!")
        return
    else:
        if data_file.endswith(".xlsx"):
            print("Dataset is: excel file")
            data = pd.read_excel(data_file)
        
        elif data_file.endswith('.csv'):
            print("Dataset is: csv file!")
            data = pd.read_csv(data_file, encoding_errors='ignore')

        else:
            print("Invalid file type")
            return
    return data

# duplicates and total_number of duplicates count
def check_duplicates(file_exist):
    duplicate = file_exist.duplicated()
    total_duplicates = file_exist.duplicated().sum()
    return duplicate, total_duplicates

# removing duplicated rows from the file and saving new files as removed_dup [duplicated rows are recorder in 'sales_data_duplicated.csv']
def remove_duplicates(duplicate, total_duplicates, file_exist, data_name):
    if total_duplicates > 0:
        list_of_duplicates = file_exist[duplicate]
        list_of_duplicates.to_csv(f"{data_name}_duplicates.csv", index=None)

    df = file_exist.drop_duplicates()
    return df

#finding missing values
def missing_values(removed_dup):
    total_missing_value = removed_dup.isnull().sum().sum()
    missing_value_colums = removed_dup.isnull().sum()
    return total_missing_value, missing_value_colums

# if dataType of column is (int, float). fill missing values with mean of that column
# else drop that column
def full_missing_values(removed_dup):
    columns = removed_dup.columns
    for col in columns:
        if removed_dup[col].dtype in (int, float):
            removed_dup[col].fillna(removed_dup[col].mean(), inplace=True)
        else:
            removed_dup.dropna(subset=col, inplace=True)
    return removed_dup


# Main function
def clean_dataset(data_file, data_name):

   
    file_exist = check_file_exist(data_file)
    print(file_exist)
    print(f"Dataset contain total rowns {file_exist.shape[0]} \nTotal columns: {file_exist.shape[1]}")

    
    [duplicate, total_duplicates] = check_duplicates(file_exist)
    print(f"Datasets has total duplicates records: {total_duplicates}")

    removed_dup = remove_duplicates(duplicate, total_duplicates,  file_exist, data_name)
    print("newdataSet: \n",removed_dup)

    
    [total_missing_value, missing_value_colums] = missing_values(removed_dup)
    print(f"Dataset has total missing value: {total_missing_value}")
    print(f"Dataset contain mmissing value by column:\n{missing_value_colums}")


    #dealing with missing values
    df = full_missing_values(removed_dup)

    print(f"Congrats! Dataset is cleaned ! \nNumber of rows: {df.shape[0]} Number of columns: {df.shape[1]}")
    df.to_csv(f'{data_name}_Cleaned_data.csv', index=None)
    print("Dataset is saved!")

    
if __name__ == '__main__':
    clean_dataset('salesdatas.xlsx', 'sales_data')
