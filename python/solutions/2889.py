import pandas as pandas

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    '''pivot the data so each row represent the temperature for each specific month and each city is a separate column

    Args: 
        weather (pd.DataFrame): The dataframe to pivot.

    Returns:
        pd.DataFrame: The pivoted dataframe.
    '''
    return weather.pivot(index='month', columns='city', values='temperature')


