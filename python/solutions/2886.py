import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    '''Change the grade column to integer

    Args:
        students (pd.DataFrame): The dataframe to change the data type of the grade column in.

    Returns:
        pd.DataFrame: The dataframe with the grade column changed to integer.
    '''
    students['grade'] = students['grade'].astype(int)
    return students

