import random
import time
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

TOPIC_SPRINKLER = "farm/sprinkler"
TOPIC_ALERT = "farm/alert"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

soil = 45
tank = 80

while True:

    soil += random.randint(-10, 5)
    soil = max(20, min(90, soil))

    tank += random.randint(-2, 0)
    tank = max(0, tank)

    if soil < 50 and tank > 10:
        sprinkler = True
    else:
        sprinkler = False

    status = "ON" if sprinkler else "OFF"

    client.publish(TOPIC_SPRINKLER, status)

    if sprinkler:
        msg = f"Sprinkler ON Soil={soil} Tank={tank}"
        client.publish(TOPIC_ALERT, msg)
        print(msg)
    else:
        print(f"Sprinkler OFF Soil={soil}")

    time.sleep(5)
