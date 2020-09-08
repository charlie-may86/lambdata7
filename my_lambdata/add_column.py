# Single function to take a list, turn it into a series
# and add it to a dataframe as a new column
import pandas as pd


def add_column(X, Y):
    """[  This function takes in a list and converts it to a
    pandas series and then adds it to a dataframe as a
    new column]

    Args:
        X ([X]): [list]
        Y ([Y]): [the dataframe you want to ammend the series to]
    """

    new_column = pd.Series(X)

    Y['new_column'] = new_columnad
