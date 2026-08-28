import pandas as pd
import numpy as np

df = pd.read_csv("data/logistics_week4_dataset.csv")
df["Traffic_Score"] = df["Traffic_Level"].map({"Low": 0, "Medium": 1, "High": 2})

# Features and target
X = df[["Distance_km", "Packages", "Traffic_Score"]].to_numpy()
y = df["Actual_Time_min"].to_numpy()

# 80/20 train-test split
rng = np.random.default_rng(7)
idx = np.arange(len(df))
rng.shuffle(idx)
cut = int(len(df) * 0.80)
train_idx, test_idx = idx[:cut], idx[cut:]

# Linear regression using least squares
X1 = np.c_[np.ones(len(X)), X]
beta = np.linalg.lstsq(X1[train_idx], y[train_idx], rcond=None)[0]
pred = X1[test_idx] @ beta

mae = np.mean(np.abs(pred - y[test_idx]))
rmse = np.sqrt(np.mean((pred - y[test_idx]) ** 2))
r2 = 1 - np.sum((y[test_idx] - pred) ** 2) / np.sum((y[test_idx] - y[test_idx].mean()) ** 2)

print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R-squared:", round(r2, 3))

# Simple vehicle allocation optimization
capacity = {"Bike": 10, "Van": 25, "Truck": 50}
cost_per_km = {"Bike": 3.5, "Van": 5.0, "Truck": 6.5}
fixed_cost = {"Bike": 30, "Van": 70, "Truck": 120}

def choose_vehicle(packages, distance):
    feasible = [v for v in capacity if capacity[v] >= packages]
    return min(feasible, key=lambda v: fixed_cost[v] + cost_per_km[v] * distance)

df["Recommended_Vehicle"] = [
    choose_vehicle(p, d) for p, d in zip(df["Packages"], df["Distance_km"])
]
print(df[["Order_ID", "Packages", "Distance_km", "Recommended_Vehicle"]].head())
