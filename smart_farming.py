import os
import random
import time
import csv
from datetime import datetime

file_exists = os.path.isfile("farm_data.csv")
file = open("farm_data.csv", "a", newline="")
writer = csv.writer(file)

if not file_exists:
    writer.writerow([
        "time",
        "temp",
        "humidity",
        "soil",
        "tank",
        "flow",
        "fertilizer",
        "pesticide",
        "stress",
        "yield"
    ])
soil = 60
tank = 80
irrigation = 0

while True:

    temp = random.randint(25, 35)
    humidity = random.randint(50, 85)

    soil += random.randint(-3, 3)
    soil = max(20, min(90, soil))

    tank += random.randint(-2, 0)
    tank = max(0, tank)

    flow = random.uniform(0, 2)

    # stress
    stress = 0
    if soil < 35 or soil > 85:
        stress += 1
    if temp > 33:
        stress += 1
    if humidity > 80:
        stress += 1

    # fertilizer
    fertilizer = 3
    if soil < 40:
        fertilizer += 2
    if temp > 33:
        fertilizer += 1

    # pesticide
    pesticide = 2
    if humidity > 80:
        pesticide += 3
    if soil > 70:
        pesticide += 2

    # yield
    yield_score = 100 - stress * 10

    now = datetime.now()

    writer.writerow([
        now,
        temp,
        humidity,
        soil,
        tank,
        flow,
        fertilizer,
        pesticide,
        stress,
        yield_score
    ])

    file.flush()

    print("Logged", now)

    time.sleep(10)
