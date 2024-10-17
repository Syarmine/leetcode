import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    '''Melt the data so each rows represent sales data for product in specific quarter 

    Args: 
        report (pd.DataFrame): The dataframe to melt.

    Returns:
        pd.DataFrame: The melted dataframe.
    '''
    return report.melt(id_vars=['product'], value_vars=['quarter_1', 'quarter_2','quarter_3','quarter_4'], 
                       var_name='quarter', value_name='sales')

