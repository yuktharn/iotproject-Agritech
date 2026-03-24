import pandas as pd

# Read CSV
data = pd.read_csv("farm_data.csv")

# Remove repeated header rows if they exist
data = data[data["temp"] != "temp"]

# Convert needed columns to numeric
numeric_cols = [
    "temp", "humidity", "soil", "tank", "flow",
    "fertilizer", "pesticide", "stress", "yield"
]

for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Drop bad rows
data = data.dropna()

print("=========== SMART FARM REPORT ===========")
print(f"Total Records Collected: {len(data)}")
print(f"Average Temperature: {data['temp'].mean():.2f} C")
print(f"Average Humidity: {data['humidity'].mean():.2f} %")
print(f"Average Soil Moisture: {data['soil'].mean():.2f} %")
print(f"Average Tank Level: {data['tank'].mean():.2f} %")
print(f"Average Yield Score: {data['yield'].mean():.2f} %")
print(f"Total Water Flow Value: {data['flow'].sum():.2f}")
print(f"Total Fertilizer Recommended: {data['fertilizer'].sum():.2f} g")
print(f"Total Pesticide Recommended: {data['pesticide'].sum():.2f} ml")
print(f"High Stress Cases: {len(data[data['stress'] >= 2])}")
print(f"Irrigation Needed Cases: {len(data[data['soil'] < 40])}")
print("=========================================")
