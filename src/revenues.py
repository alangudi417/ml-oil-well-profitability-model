import pandas as pd
import numpy as np

def revenue(target, predictions, count, ingreso_unidad, inversion):

    # Sort predictions from highest to lowest
    predictions_sorted = predictions.sort_values(ascending=False)

    # Select top indexes
    top_indexes = predictions_sorted.index[:count]

    # Select top targets and predictions
    target_top = target.loc[top_indexes]

    # Calculate potential profit
    profit = target_top.sum() * ingreso_unidad - inversion
    return profit