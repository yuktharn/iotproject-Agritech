# Smart Precision Farming using IoT with Alert and Recommendation System

## Overview
This project is a **Smart Precision Farming System** developed using **Raspberry Pi**, **Python**, **MQTT**, **Google Sheets**, **Flask Web Server**, **LED**, and **16x2 I2C LCD**.

The system simulates agricultural sensor data such as:

- Soil Moisture
- Temperature
- Humidity
- Tank Level
- Water Flow

Based on these values, the system performs:

- Sprinkler ON/OFF decision
- LED alert when soil is dry
- LCD status display
- Data logging in CSV
- Data analysis and graph generation
- Alert generation
- Yield prediction
- Fertilizer recommendation
- Pesticide recommendation
- MQTT-based mobile alerting
- Web dashboard display

This project focuses on **analysis, monitoring, and smart farming decision support**.

---

## Features

- Real-time simulated farm data generation every **10 seconds**
- CSV data logging
- Google Sheets integration
- Flask-based web dashboard
- MQTT alerts to mobile using **IoT MQTT Panel**
- LED alert for dry soil
- LCD display for sprinkler status
- Smart recommendations for:
  - Fertilizer
  - Pesticide
- Stress level calculation
- Yield score calculation
- Graph generation for analysis
- Prediction module for future farm conditions

---

## Technologies Used

### Hardware
- Raspberry Pi
- 16x2 I2C LCD
- LED
- Resistor
- Breadboard
- Jumper wires

### Software
- Python
- Flask
- Pandas
- Matplotlib
- MQTT
- Mosquitto
- Google Sheets
- RPLCD
- gpiozero

---

## Project Structure

```bash
smart_farming.py      # main simulation and CSV logging
analysis.py           # graph generation and analysis
alerts.py             # alerts and recommendations
report.py             # summary report generation
prediction.py         # future prediction module
combined_graph.py     # combined graph generation
webserver.py          # Flask dashboard
mqtt_farm.py          # MQTT alerts for mobile app
lcd_test.py           # LCD testing
lcd_led_farm.py       # LCD + LED + sprinkler logic
farm_data.csv         # generated dataset
final_report.txt      # generated report
final_alerts.txt      # generated alert log
final_prediction.txt  # generated prediction log
static/               # graph images for web dashboard

---

## Working Principle

1. Raspberry Pi generates simulated farm sensor values every 10 seconds.
2. Data is stored in farm_data.csv.
3. The system analyzes soil, temperature, humidity, tank level, and water flow.
4. Based on thresholds:
      sprinkler status is decided
      LED is turned ON/OFF
      LCD displays sprinkler status
5. Alerts are generated when:
      soil is too dry
      humidity is high
      tank level is low
      stress is high

---

## Recommendations are generated for:

1. fertilizer
2. pesticide
3. Data is visualized in graphs and shown in the web dashboard.
4. MQTT alerts are sent to mobile phone through IoT MQTT Panel.

---

## Performance Metrics

The project evaluates:
1. Average Temperature
2. Average Humidity
3. Average Soil Moisture
4. Average Yield Score
5. Total Water Usage
6. Total Fertilizer Recommendation
7. Total Pesticide Recommendation
8. High Stress Count
9. Irrigation Needed Count

---

## Applications

1. Smart irrigation
2. Precision agriculture
3. Greenhouse monitoring
4. IoT-based farming research
5. Water-saving agriculture systems
6. Agricultural data analytics

---

## Future Improvements

1. Add real soil moisture sensor
2. Add real tank level sensor
3. Add camera for crop disease detection
4. Add machine learning model
5. Add cloud dashboard
6. Add solar-powered deployment
7. Add multiple farm zones
8. Add real relay-controlled sprinkler hardware

---

## Author

RASHMITHA S
CHINMAYI MOHAN
YUKTHA R N
Smart Precision Farming Project
