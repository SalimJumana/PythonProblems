import pandas as pd

# Run shortcut in PyCharm: shift + Fn key + F10

# To read a csv file in pandas, we simply use -> pd.read_csv('data.csv')

#1 reading the content of this file (with header) and storing it in a dataframe
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv')

# while reading path location of file, if python IDE gives error because it is reading (\) backslash as special
# character, then just write path in raw string format, that is, r"folder\file\data.csv"
# header is bydefault True

# to see contents of the file
print(df)

# 2 read file without Header
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', header=None)
print(df)

#3 read file - add Column names
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', names=['ID', 'FN', 'LN'])
print(df)

#4 read file - skip header, add column names
# since in our raw data, we have a header row, in above example it is printed as a data row and now
# we want to skip it and give our own header names
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', skiprows=1, names=['ID', 'FN', 'LN'])
print(df)


#5 Read file - only specific columns using names
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', usecols=['FirstName', 'LastName'])
print(df)

#6 Read file - only specific columns using column index
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', usecols=[1,2])
print(df)

#7 Read csv files without index
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', index_col=None)
print(df)
# df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', index_col=False) -> works the same
# Reading file without index is the default.

# lets see when dataframe reads this data from csv, what data type it interprets all these columns as
print(df.dtypes)

#8 Read csv file - change column data types
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', dtype={'CustomerID': 'float32'})
print(df.dtypes)

#9 Read csv first col as index
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', index_col=0)
print(df)
# this makes first column i.e CustomerID as the index column

#10 - Read csv missing values
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', na_values=['Brenda'])
print(df)
# this writes 'NaN' in place of the string you assign to na_values' parameter
# blank spaces it reads by default as 'NaN'

#11 Read csv - remove last 2 rows
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', engine='python', skipfooter=2)
print(df)
# providing 'engine=python' bcoz "C" engine does not support skipfooter

#12 Read csv skip rows
# skipping two rows from the top (of the data in the file)
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', skiprows=2)
print(df)

# it skips rows with index no 1 and 3
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', skiprows=[1,3])
print(df)

# skipping a range of records
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', skiprows=range(1,3))
print(df)

#13 if delimiter(separator) is some character (but not comma) -- say | (pipe)
df1 = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers_pipe.csv', sep='|')
print(df1)

#14 Read csv - use second row as header
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', header=1)
print(df)

#15 Read first n rows
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv', nrows=3)
print(df)

#16 Read csv - all columns as string
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv',dtype = str)
print(df.dtypes)

#17 - Read csv - all except few columns as string
df = pd.read_csv('G:\DOWNLOADS\sample datasets\Customers.csv',dtype='float64', converters={'FirstName': str, 'LastName': str})
print(df.dtypes)
