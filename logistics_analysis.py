"""
Week 1 Logistics Project
Logistics Route Optimization and Delivery Performance Analysis

This script demonstrates the proposed Week 1 analytical workflow.
The included dataset is simulated for demonstration and learning.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Load data
data = pd.read_csv("data/sample_logistics_data.csv")

# 2. Basic cleaning
data = data.drop_duplicates()
data["Distance_km"] = pd.to_numeric(data["Distance_km"], errors="coerce")
data["Actual_Time_min"] = pd.to_numeric(data["Actual_Time_min"], errors="coerce")
data = data.dropna(subset=["Distance_km", "Actual_Time_min", "Packages"])

# 3. KPI calculation
total_deliveries = len(data)
on_time_rate = data["On_Time"].mean() * 100
average_distance = data["Distance_km"].mean()
average_delivery_time = data["Actual_Time_min"].mean()
average_delivery_cost = data["Delivery_Cost"].mean()
vehicle_utilization = (data["Packages"] / data["Vehicle_Capacity"]).mean() * 100

print("Logistics KPI Summary")
print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")
print(f"Average Delivery Distance: {average_distance:.2f} km")
print(f"Average Delivery Time: {average_delivery_time:.2f} minutes")
print(f"Average Delivery Cost: {average_delivery_cost:.2f}")
print(f"Average Vehicle Utilization: {vehicle_utilization:.2f}%")

# 4. Exploratory Data Analysis
plt.figure()
plt.hist(data["Actual_Time_min"])
plt.xlabel("Actual Delivery Time (minutes)")
plt.ylabel("Number of Deliveries")
plt.title("Delivery Time Distribution")
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(data["Distance_km"], data["Actual_Time_min"])
plt.xlabel("Distance (km)")
plt.ylabel("Actual Delivery Time (minutes)")
plt.title("Distance vs Delivery Time")
plt.tight_layout()
plt.show()

# 5. Regression: predict delivery time
X = data[["Distance_km", "Packages"]]
y = data["Actual_Time_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)
predicted_time = regression_model.predict(X_test)

mae = mean_absolute_error(y_test, predicted_time)
rmse = mean_squared_error(y_test, predicted_time) ** 0.5

print(f"Regression MAE: {mae:.2f} minutes")
print(f"Regression RMSE: {rmse:.2f} minutes")

# 6. Clustering: customer/delivery segmentation
cluster_features = data[["Distance_km", "Packages"]]
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data["Cluster"] = kmeans.fit_predict(cluster_features)

print("\nCluster counts:")
print(data["Cluster"].value_counts().sort_index())

# 7. Route optimization plan
# For a full implementation, create a distance/travel-time matrix and
# solve the Vehicle Routing Problem using Google OR-Tools.
#
# Steps:
#   a. Create distance matrix
#   b. Define vehicles and capacities
#   c. Add customer demand
#   d. Add time windows if available
#   e. Minimize total travel distance/cost
#   f. Solve and export optimized routes

print("\nNext phase: implement vehicle routing with Google OR-Tools.")
