import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    '''Find the animals with weight greater than 100kg

    Args:
        animals (pd.DataFrame): The dataframe to find the animals in.

    Returns:
        pd.DataFrame: name column with the animals with weight greater than 100kg, sorted by weight in descending order.
    '''
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

