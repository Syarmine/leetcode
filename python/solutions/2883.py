import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    '''Write a solution to remove the rows with missing data from the 'name' column

    Args:
        students (pd.DataFrame): The dataframe to remove the rows with missing data from the 'name' column

    Returns:
        pd.DataFrame: The dataframe with the rows with missing data removed.
    '''
    return students.dropna(subset=['name'])

