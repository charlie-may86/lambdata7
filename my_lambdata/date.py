import pandas as pd
# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

def date_columns(X):
  '''
  Change the name of your date columne to 'Date'
  '''

  #create a year column
  X['year'] = pd.DatetimeIndex(X['Date']).year

  #create a month column
  X['month'] = pd.DatetimeIndex(X['Date']).month

  #create a day column
  X['day'] = pd.DatetimeIndex(X['Date']).day