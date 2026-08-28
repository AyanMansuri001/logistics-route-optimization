import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/logistics_week3_dataset.csv")
df["Delay_min"] = df["Actual_Time_min"] - df["Expected_Time_min"]

print(df.describe())
print("On-time rate:", round(df["On_Time"].mean()*100,2), "%")
print("Average cost:", round(df["Delivery_Cost"].mean(),2))
print("Average delay:", round(df["Delay_min"].mean(),2))

zone_summary = df.groupby("Zone")["Delay_min"].mean()
zone_summary.plot(kind="bar", title="Average Delivery Delay by Zone")
plt.ylabel("Minutes"); plt.tight_layout(); plt.show()

plt.scatter(df["Distance_km"], df["Actual_Time_min"])
plt.xlabel("Distance (km)"); plt.ylabel("Actual Time (minutes)")
plt.title("Distance vs Actual Delivery Time"); plt.tight_layout(); plt.show()

print(df[["Distance_km","Packages","Actual_Time_min","Delivery_Cost","Delay_min","On_Time"]].corr())
