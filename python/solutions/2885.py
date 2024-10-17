import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    '''Rename the columns 'id' to 'student_id' and 'first' to 'first_name' and 'last' to 'last_name' and 'age' to 'age_in_years'

    Args:
        students (pd.DataFrame): The dataframe to rename the columns of.

    Returns:
        pd.DataFrame: The dataframe with the columns renamed.
    '''
    return students.rename(columns={
        'id': 'student_id', 
        'first':'first_name', 
        'last':'last_name', 
        'age':'age_in_years'}) 
