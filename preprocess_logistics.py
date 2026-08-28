"""
Week 2 Task - Data Collection, Cleaning and Preprocessing for Logistics Analysis

The raw dataset is simulated for demonstration. The workflow intentionally
contains common data-quality issues so that the preprocessing steps can be
demonstrated clearly.
"""

import pandas as pd
import numpy as np

# 1. Simulated data collection
data = pd.read_csv("data/raw_logistics_data.csv")

print("Raw shape:", data.shape)
print("\nMissing values before cleaning:")
print(data.isna().sum())

# 2. Remove duplicate records
data = data.drop_duplicates()

# 3. Standardize categorical text
data["Vehicle_Type"] = (
    data["Vehicle_Type"].astype(str).str.strip().str.title()
)
data["Customer_Zone"] = (
    data["Customer_Zone"].astype(str).str.strip().str.title()
)

# 4. Convert invalid values to missing
data.loc[data["Distance_km"] <= 0, "Distance_km"] = np.nan
data.loc[data["Delivery_Cost"] <= 0, "Delivery_Cost"] = np.nan
data.loc[~data["On_Time"].isin([0, 1]), "On_Time"] = np.nan

# 5. Convert numeric columns and handle missing values
numeric_cols = [
    "Distance_km", "Packages", "Expected_Time_min",
    "Actual_Time_min", "Delivery_Cost"
]

for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")
    data[col] = data[col].fillna(data[col].median())

# 6. Detect and cap outliers using the IQR method
outlier_cols = [
    "Distance_km", "Packages", "Actual_Time_min", "Delivery_Cost"
]

for col in outlier_cols:
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    data[col] = data[col].clip(lower, upper)

# 7. Handle missing/invalid binary values
data["On_Time"] = data["On_Time"].fillna(
    data["On_Time"].mode()[0]
).astype(int)

# 8. Rebuild vehicle capacity after standardizing vehicle type
capacity_map = {
    "Van": 25,
    "Truck": 50,
    "Mini Truck": 15
}
data["Vehicle_Capacity"] = data["Vehicle_Type"].map(capacity_map)

# 9. Min-Max normalization
for col in ["Distance_km", "Packages", "Actual_Time_min", "Delivery_Cost"]:
    minimum = data[col].min()
    maximum = data[col].max()
    data[col + "_Normalized"] = (
        (data[col] - minimum) / (maximum - minimum)
    )

# 10. Save the processed dataset
data.to_csv(
    "outputs/cleaned_normalized_logistics_data.csv",
    index=False
)

print("\nPreprocessing complete.")
print("Cleaned shape:", data.shape)
print("\nMissing values after cleaning:")
print(data.isna().sum())
