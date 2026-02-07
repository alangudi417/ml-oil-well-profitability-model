import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Model Function:
def entrenar_y_evaluar_modelo(dataset):

    # Split features and target:
    features = dataset.drop(['product'], axis=1)
    target = dataset['product']

    # Split data into training and validation sets:
    features_train, features_valid, target_train, target_valid = train_test_split(
        features, target, test_size=0.25, random_state=42
    )

    # Model training and prediction:
    model = LinearRegression()
    model.fit(features_train, target_train)
    predictions = pd.Series(
        model.predict(features_valid),
        index=target_valid.index
    )

    # Metrics
    mse = mean_squared_error(target_valid, predictions)
    rmse = mse ** 0.5
    mean_predicted_volume = predictions.mean()

    # Final results
    print(f"Average volume: {mean_predicted_volume:.5f}")
    print(f"RMSE: {rmse:.5f}")

    return predictions, target_valid, rmse