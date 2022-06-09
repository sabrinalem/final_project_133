import pandas as pd

# import data
billboards_data = pd.read_csv("data/billboards/billboards_data.csv")
grammys_data = pd.read_csv("data/grammys/grammys_data.csv")

# merge and tidy data frames 
combine = pd.merge(billboards_data, grammys_data, how='right')


combine_ = pd.merge(billboards_data, combine, how='outer')
combine_['Position'].fillna(101, inplace=True)
combine_['Win'].fillna(0, inplace=True)

# send data frame to CSV file
combine_.to_csv('combine.csv')

