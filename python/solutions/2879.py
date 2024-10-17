import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    ''' Display the first three rows of the dataframe

    Args:
        employees (pd.DataFrame): The dataframe to display the first three rows of.

    Returns:
        pd.DataFrame: The first three rows of the dataframe.
    '''
    return employees.head(3)
