import pandas as pd
import numpy as np

def drop_id(df, name=None):
    df_clean = df.drop(['id'], axis=1)

    print(df_clean.columns)
    return df_clean