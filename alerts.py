import pandas as pd

data = pd.read_csv("farm_data.csv")

last = data.iloc[-1]

# convert to numbers
temp = float(last["temp"])
humidity = float(last["humidity"])
soil = float(last["soil"])
tank = float(last["tank"])
flow = float(last["flow"])
fertilizer = float(last["fertilizer"])
pesticide = float(last["pesticide"])
stress = int(last["stress"])
yield_score = float(last["yield"])

print("------ CURRENT FARM STATUS ------")
print(f"Temperature: {temp}")
print(f"Humidity: {humidity}")
print(f"Soil Moisture: {soil}")
print(f"Tank Level: {tank}")
print(f"Flow Rate: {flow}")
print(f"Fertilizer Recommendation: {fertilizer} g")
print(f"Pesticide Recommendation: {pesticide} ml")
print(f"Stress Level: {stress}")
print(f"Yield Score: {yield_score}%")
print("---------------------------------")

print("\nALERTS / RECOMMENDATIONS:")

alert_found = False

if soil < 40:
    print("ALERT: Soil moisture is low. Irrigation needed.")
    alert_found = True

if tank < 20:
    print("ALERT: Tank level low.")
    alert_found = True

if temp > 33:
    print("ALERT: High temperature.")
    alert_found = True

if humidity > 80:
    print("ALERT: High humidity. Disease risk.")
    alert_found = True

if flow < 0.5 and soil < 40:
    print("ALERT: Low water flow.")
    alert_found = True

if stress >= 2:
    print("ALERT: Crop stress high.")
    alert_found = True

if fertilizer > 4:
    print(f"RECOMMEND: Add {fertilizer} g fertilizer.")
    alert_found = True

if pesticide > 4:
    print(f"RECOMMEND: Add {pesticide} ml pesticide.")
    alert_found = True

if yield_score < 80:
    print("ALERT: Yield dropping.")
    alert_found = True

if not alert_found:
    print("System normal.")
