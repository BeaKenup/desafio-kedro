"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.4
"""

import pandas as pd

def preprocess_titanic(dt_titanic:pd.DataFrame):
    dt_titanic = dt_titanic.drop(columns=['Pclass','Fare','Ticket','Cabin'])
    dt_titanic = dt_titanic.dropna()
    return dt_titanic