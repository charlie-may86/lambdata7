from pandas import DataFrame


def add_state_names_column(my_df):
    """[This functions adds a column of corresponding state names to a df
    that has state abbrv]
    """
    new_df = my_df.copy()

    names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Conn'}

    new_df['name'] = my_df['abbrev'].map(names_map)

    return new_df


if __name__ == "__main__":

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    mapped_df = add_state_names_column(df)
    print(mapped_df.head())