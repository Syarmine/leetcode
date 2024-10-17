import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    ''' Row filter where students.['student_id'] is 101
    Args:
        students (pd.DataFrame): The dataframe to filter.

    Returns:
        pd.DataFrame: A dataframe containing the rows where students.['student_id'] is 101.
    '''
    return students.loc[students['student_id'] == 101, ["name", "age"]]
