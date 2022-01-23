from argparse import Action
from operator import truediv
from urllib.request import DataHandler
from matplotlib.pyplot import title
import numpy as np
import pandas as pd
import time


# open the .csv file
df = pd.read_csv('movies.csv')

# ask user for input
view = input('Do you want to view the data? (Yes/No)')

# Display data for user to view

if input == 'yes' or 'Yes':

     lines = int(input('How many lines do you want?: '))
   
     input('press Enter to start diplaying data...')

     print(df.head(lines))

     more = str(input('how many more? (920 total)'))

     print(df.head(more))

     more_1 = str(input('how many more? (920 total)'))

     print(df.head(more_1))

     more_2 = str(input('how many more? (920 total)'))

     print(df.head(more_2))

else: sort = input('Do you want to sort the data? (Yes/No)')


if sort == "yes" or "Yes":

     initial_sort = input('Which colomun do you want to sort the data? (Title, Movie Info, Release Date, Domestic Sales (In $), Genre): ')

# Sort by given column input

     if initial_sort == str('Title'):

         print (df.sort_values(by='Title'))

     elif initial_sort == str('Movie Info'):

         print (df.sort_values(by='Movie Info'))

     elif initial_sort == str('Release Date'):

         print (df.sort_values(by='Release Date'))
    
     elif initial_sort == str('Domestic Sales (In $)'):

         print (df.sort_values(by='Domestic Sales (In $)'))
     elif initial_sort == str('Genre'):

         print (df.sort_values(by='Genre'))

# Query function

print('Films that grossed over a million dollars:')
# Eliminates the spaces in the column names

df.columns =[column.replace(" ", "_") for column in df.columns]

initial_query = input("Enter Search Parameter or press enter to quit:")

df.drop(df.columns[[1, 2]], axis=1, inplace=False)

df1 = df[['Title','Domestic_Sales']]

# Query the Data
print(df.query('Domestic_Sales > 1000000', inplace=False))    
