# Week 4 - Predictive Modeling and Optimization in Logistics

This educational project predicts actual delivery time and proposes a simple vehicle-allocation optimization strategy.

## Files
- `data/logistics_week4_dataset.csv` — hypothetical logistics dataset
- `src/week4_predictive_optimization.py` — model and optimization code
- `visualizations/` — model and optimization charts
- `report/Week_4_Logistics_Predictive_Modeling_and_Optimization_Report.docx` — final report

## Target
Actual delivery time (minutes).

## Features
Distance, package count, and traffic level.

## Model
Linear regression using an 80/20 train-test split.

## Metrics
MAE, RMSE, and R-squared.

## Optimization
Select the lowest estimated-cost vehicle that has sufficient capacity for the order.

The dataset is simulated for educational purposes.
