import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:  
    '''Write a solution to drop these duplicate rows and keep only the first occurence

    Args:
        customers (pd.DataFrame): The dataframe to drop duplicate rows from.

    Returns:
        pd.DataFrame: The dataframe with duplicate rows dropped.
    '''
    return customers.drop_duplicates(subset=['email'], keep='first')

