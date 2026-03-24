import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("farm_data.csv")

# Remove repeated header rows if present
data = data[data["temp"] != "temp"]

# Convert numeric columns properly
numeric_cols = [
    "temp", "humidity", "soil", "tank", "flow",
    "fertilizer", "pesticide", "stress", "yield"
]

for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Drop bad rows
data = data.dropna()

print("Total records:", len(data))

# Averages
avg_temp = data["temp"].mean()
avg_soil = data["soil"].mean()
avg_hum = data["humidity"].mean()
avg_yield = data["yield"].mean()

print("Average Temp:", round(avg_temp, 2))
print("Average Soil:", round(avg_soil, 2))
print("Average Humidity:", round(avg_hum, 2))
print("Average Yield:", round(avg_yield, 2))

# Irrigation need count
low_soil = data[data["soil"] < 40]
irrigations = len(low_soil)
print("Irrigation needed times:", irrigations)

# Fertilizer and pesticide totals
fert_total = data["fertilizer"].sum()
pest_total = data["pesticide"].sum()

print("Total fertilizer used:", round(fert_total, 2))
print("Total pesticide used:", round(pest_total, 2))

# Stress analysis
stress_high = len(data[data["stress"] >= 2])
print("High stress count:", stress_high)

# Water usage
flow_total = data["flow"].sum()
print("Total water used:", round(flow_total, 2))

# Graphs
plt.figure()
plt.plot(data["temp"])
plt.title("Temperature")
plt.xlabel("Records")
plt.ylabel("Temperature")
plt.savefig("temp.png")

plt.figure()
plt.plot(data["soil"])
plt.title("Soil Moisture")
plt.xlabel("Records")
plt.ylabel("Soil Moisture")
plt.savefig("soil.png")

plt.figure()
plt.plot(data["yield"])
plt.title("Yield Score")
plt.xlabel("Records")
plt.ylabel("Yield")
plt.savefig("yield.png")

plt.figure()
plt.plot(data["fertilizer"])
plt.title("Fertilizer Recommendation")
plt.xlabel("Records")
plt.ylabel("Fertilizer")
plt.savefig("fertilizer.png")

plt.figure()
plt.plot(data["pesticide"])
plt.title("Pesticide Recommendation")
plt.xlabel("Records")
plt.ylabel("Pesticide")
plt.savefig("pesticide.png")

print("Graphs saved successfully")
