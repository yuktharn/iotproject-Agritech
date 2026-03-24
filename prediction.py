import pandas as pd

data = pd.read_csv("farm_data.csv")

data = data[data["temp"] != "temp"]

numeric_cols = [
    "temp", "humidity", "soil", "tank", "flow",
    "fertilizer", "pesticide", "stress", "yield"
]

for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")

data = data.dropna()

if len(data) < 2:
    print("Not enough data for prediction.")
    exit()

last_soil = data["soil"].iloc[-1]
prev_soil = data["soil"].iloc[-2]

last_yield = data["yield"].iloc[-1]
prev_yield = data["yield"].iloc[-2]

soil_change = last_soil - prev_soil
yield_change = last_yield - prev_yield

predicted_soil = last_soil + soil_change
predicted_yield = last_yield + yield_change

print("======= PREDICTION REPORT =======")
print(f"Current Soil Moisture: {last_soil:.2f}")
print(f"Predicted Next Soil Moisture: {predicted_soil:.2f}")

if predicted_soil < 40:
    print("Prediction: Irrigation may be needed soon.")
else:
    print("Prediction: Soil condition looks stable.")

print(f"Current Yield Score: {last_yield:.2f}")
print(f"Predicted Next Yield Score: {predicted_yield:.2f}")
print("=================================")
