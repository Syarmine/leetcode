import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    '''Fill missing value as 0 in the quantity column

    Args:
        products (pd.DataFrame): The dataframe to fill the missing values in.

    Returns:
        pd.DataFrame: The dataframe with the missing values filled.
    '''
    products['quantity'] = products['quantity'].fillna(0)
    return students

