import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    ''' Create a new column 'bonus' that contains the doubled values from salary column

    Args:
        employees (pd.DataFrame): The dataframe to create the new column in.

    Returns:
        pd.DataFrame: The dataframe with the new column.
    '''
    employees['bonus'] = employees['salary'] * 2
    return employees
