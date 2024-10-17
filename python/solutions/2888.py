import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    '''Concatenate two DataFrame vertically into one DataFrame
    
    Args:
        df1 (pd.DataFrame): The first dataframe to concatenate.
        df2 (pd.DataFrame): The second dataframe to concatenate.

    Returns:
        pd.DataFrame: The concatenated dataframe.
    '''
    return pd.concat([df1, df2], axis=0)


