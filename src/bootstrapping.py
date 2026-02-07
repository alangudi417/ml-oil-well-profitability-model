import pandas as pd

# Bootstrapping for Risk Assessment
def risk_calculation(
        target, 
        predictions, 
        revenue_func, 
        ingreso_unidad, 
        inversion, 
        n_bootstrap=1000,
        sample_size=500,
        top_n=200):
    
    # Empty list
    values = []

    # Bootstrapping repeated n_bootstrap (1000) times.
    for i in range(n_bootstrap):

        # According to requirements, sampling must be 500 points
        target_subsample = target.sample(n=sample_size, replace=True, random_state=i)

        # Corresponding predictions
        predictions_subsample = predictions.loc[target_subsample.index]

        # Profit from top 200 wells
        profit = revenue_func(
            target_subsample, 
            predictions_subsample, 
            top_n, 
            ingreso_unidad, 
            inversion)
        
        values.append(profit)
    values = pd.Series(values)

    # Final metrics
    mean = values.mean()
    lower = values.quantile(0.025)  # 2.5% confidence
    upper = values.quantile(0.975)  # 97.5% confidence
    risk = (values < 0).mean() * 100
    
    return mean, lower, upper, risk, values