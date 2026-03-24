import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("farm_data.csv")
data = data[data["temp"] != "temp"]

numeric_cols = [
    "temp", "humidity", "soil", "tank", "flow",
    "fertilizer", "pesticide", "stress", "yield"
]

for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")

data = data.dropna()

plt.figure(figsize=(10, 6))
plt.plot(data["soil"], label="Soil Moisture")
plt.plot(data["yield"], label="Yield Score")
plt.plot(data["temp"], label="Temperature")
plt.legend()
plt.title("Combined Smart Farming Analysis")
plt.xlabel("Records")
plt.ylabel("Values")
plt.savefig("combined_graph.png")

print("Combined graph saved.")
