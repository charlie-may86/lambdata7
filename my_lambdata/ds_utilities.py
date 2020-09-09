import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint
from IPython.display import display


def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100


class My_Data_Splitter():
    def __init__(self, df, features, target):
        self.df = df
        self.features = features
        self.target = target
        self.X = df[features]
        self.y = df[target]

    def train_validation_test_split(self, train_size=0.7, val_size=0.1,
                                    test_size=0.2, random_state=None,
                                    shuffle=True):
        '''
        This function is a utility wrapper around the Scikit-Learn
        train_test_split that splits arrays or matrices into train,
        validation, and test subsets.
        Args:
            df (Pandas DataFrame): Dataframe with code.
            X (list): A list of features.
            y (str): A string with target column.
            train_size (float or int): Proportion of the dataset to include in
            the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in
            the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in
            the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data
            before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        Returns:
            Train, test, validation dataframes for features (X) and target (y).
        '''

        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state,
            shuffle=shuffle)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val,
            test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test

    def print_split_summary(self, X_train, X_val, X_test):

        print('############## TRAINING DATA ###############')
        print(f'X_train Shape: {X_train.shape}')
        display(X_train.describe(include='all').transpose())
        print('')

        print('############## VALIDATION DATA ###############')
        print(f'X_val Shape: {X_val.shape}')
        display(X_val.describe(include='all').transpose())
        print('')

        print('############## VALIDATION DATA ###############')
        print(f'X_test Shape: {X_test.shape}')
        display(X_test.describe(include='all').transpose())
        print('')

# def something(x, y):
#     """[summary]

#     Args:
#         x ([type]): [description]
#         y ([type]): [description]
#     """

'''
anything below this only runs when you run this package
if you import this package, the stuff below if __name__ == '__main__'
won't run
'''

if __name__ == '__main__':

    # Simple test for the enlarge function
    # print(enlarge(5))

    # Test fro train_validation_test_split function
    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

    # run the code below in the (Pdb) shell
    # X_train, X_val, X_test, y_train, y_val, y_test =
    # train_validation_test_split(df, features=['ash', 'hue'], target='target')

    # breakpoint()
    # test my data splitter
    splitter = My_Data_Splitter(df=df, features=['ash', 'hue'],
                                target='target')
    X_train, X_val, X_test, y_train, y_val, y_test = splitter.train_validation_test_split()
    splitter.print_split_summary(X_train, X_val, X_test)

