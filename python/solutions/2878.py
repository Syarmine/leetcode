import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    ''' Get the number of rows and columns in the dataframe

    Args:
        players (pd.DataFrame): The dataframe to get the size of.
        shape is a property of the dataframe that returns a tuple of the number of rows and columns.
        players.shape[0] returns the number of rows.
        players.shape[1] returns the number of columns.
        We can return the number of rows and columns as a list.
    Returns:
        List[int]: A list containing the number of rows and columns in the dataframe.
    '''
    return [players.shape[0], players.shape[1]]