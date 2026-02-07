# Oil Well Profitability Prediction
## 📊 Project Overview

This project develops a Machine Learning model to identify the most profitable region for drilling 200 new oil wells for OilyGiant. Using geological data from three potential regions, regression models are trained to predict oil reserve volumes and select wells with the highest estimated yields.
Expected profits and financial risks are evaluated using bootstrapping simulation, enabling a data-driven comparison of drilling locations. The ultimate goal is to recommend the region that maximizes profitability while minimizing investment risk.

## 📊 Dataset Description
The dataset contains geological exploration data from three regions, including:
•	Oil reserve volume estimates
•	Geological characteristics of wells
•	Regional production data
Each dataset represents a potential drilling region used for predictive modeling and profitability evaluation.

## ⚙️ Methodology
The project follows an end-to-end data science workflow:
1. Data Preprocessing
•	Data cleaning and validation
•	Feature selection
•	Train/test splitting
2. Model Development
•	Linear Regression models trained separately for each region
•	Prediction of oil reserve volumes for new wells
3. Model Evaluation
•	Performance measured using Root Mean Squared Error (RMSE)
•	Model precision compared across regions
4. Risk & Profitability Analysis
•	Bootstrapping simulation to estimate:
o	Expected profit distribution
o	Probability of financial losses
o	Investment risk assessment

## 📈 Project Highlights
- Built regression models to predict oil reserves
- Performed financial risk simulation using bootstrapping
- Delivered business recommendation based on data-driven insights

## 📈 Results
After evaluating predictive accuracy, profitability, and financial risk, Region 1 (geo_data_1) was identified as the optimal drilling location.

### Key Findings
- Highest Model Precision: RMSE of 0.89
- Highest Average Profit: $6'343,278.00
- Lowest Financial Risk: Probability of Loss is 0.5%

## ▶️ How to Run the Project
git clone https://github.com/alangudi417/ml-oil-well-profitability-model.git
cd ml-oil-well-profitability-model
pip install -r requirements.txt
jupyter notebook