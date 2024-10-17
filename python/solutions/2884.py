import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    '''Modify the salary column by multiplying each salary by 2

    Args:
        employees (pd.DataFrame): The dataframe to modify the salary column in.

    Returns:
        pd.DataFrame: The dataframe with the salary column modified.
    '''
    employees['salary'] = employees['salary'] * 2
    return employees

