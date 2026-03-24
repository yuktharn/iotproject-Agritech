from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    try:
        data = pd.read_csv("farm_data.csv")
        data = data[data["temp"] != "temp"]

        numeric_cols = [
            "temp", "humidity", "soil", "tank", "flow",
            "fertilizer", "pesticide", "stress", "yield"
        ]

        for col in numeric_cols:
            data[col] = pd.to_numeric(data[col], errors="coerce")

        data = data.dropna()
        last = data.iloc[-1]

        alert_text = "System Normal"
        if last["soil"] < 40:
            alert_text = "Low Soil Moisture - Irrigation Needed"
        elif last["tank"] < 20:
            alert_text = "Low Tank Level"
        elif last["humidity"] > 80:
            alert_text = "High Humidity - Disease Risk"
        elif last["temp"] > 33:
            alert_text = "High Temperature Alert"

        irrigation_needed = len(data[data["soil"] < 40])
        high_stress = len(data[data["stress"] >= 2])
        total_water = data["flow"].sum()
        total_fertilizer = data["fertilizer"].sum()
        total_pesticide = data["pesticide"].sum()

        html = f"""
        <html>
        <head>
            <title>Smart Precision Farming Dashboard</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #eef3f8;
                    padding: 20px;
                }}
                h1 {{
                    text-align: center;
                    color: #1f4e79;
                }}
                h2 {{
                    color: #1f4e79;
                    margin-top: 30px;
                }}
                .grid {{
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 15px;
                }}
                .card {{
                    background: white;
                    padding: 15px;
                    border-radius: 12px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
                .title {{
                    font-size: 16px;
                    color: #444;
                }}
                .value {{
                    font-size: 22px;
                    font-weight: bold;
                    color: #2e7d32;
                }}
                .alert {{
                    background: #fff3cd;
                    color: #856404;
                    padding: 15px;
                    border-radius: 10px;
                    margin-bottom: 20px;
                    font-weight: bold;
                }}
                .graphs img {{
                    width: 45%;
                    margin: 10px;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
            </style>
            <meta http-equiv="refresh" content="10">
        </head>
        <body>
            <h1>Smart Precision Farming Dashboard</h1>

            <div class="alert">Current Alert: {alert_text}</div>

            <h2>Current Farm Status</h2>
            <div class="grid">
                <div class="card"><div class="title">Temperature</div><div class="value">{last['temp']} °C</div></div>
                <div class="card"><div class="title">Humidity</div><div class="value">{last['humidity']} %</div></div>
                <div class="card"><div class="title">Soil Moisture</div><div class="value">{last['soil']} %</div></div>
                <div class="card"><div class="title">Tank Level</div><div class="value">{last['tank']} %</div></div>
                <div class="card"><div class="title">Flow Rate</div><div class="value">{last['flow']} L/min</div></div>
                <div class="card"><div class="title">Stress Level</div><div class="value">{last['stress']}</div></div>
                <div class="card"><div class="title">Yield Score</div><div class="value">{last['yield']} %</div></div>
                <div class="card"><div class="title">Fertilizer</div><div class="value">{last['fertilizer']} g</div></div>
                <div class="card"><div class="title">Pesticide</div><div class="value">{last['pesticide']} ml</div></div>
            </div>

            <h2>Analysis Summary</h2>
            <div class="grid">
                <div class="card"><div class="title">Average Temp</div><div class="value">{data['temp'].mean():.2f} °C</div></div>
                <div class="card"><div class="title">Average Soil</div><div class="value">{data['soil'].mean():.2f} %</div></div>
                <div class="card"><div class="title">Average Yield</div><div class="value">{data['yield'].mean():.2f} %</div></div>
                <div class="card"><div class="title">Irrigation Needed Count</div><div class="value">{irrigation_needed}</div></div>
                <div class="card"><div class="title">High Stress Count</div><div class="value">{high_stress}</div></div>
                <div class="card"><div class="title">Total Water Used</div><div class="value">{total_water:.2f}</div></div>
                <div class="card"><div class="title">Total Fertilizer</div><div class="value">{total_fertilizer:.2f} g</div></div>
                <div class="card"><div class="title">Total Pesticide</div><div class="value">{total_pesticide:.2f} ml</div></div>
                <div class="card"><div class="title">Total Records</div><div class="value">{len(data)}</div></div>
            </div>

            <h2>Generated Graphs</h2>
            <div class="graphs">
                <img src="/static/temp.png" alt="Temperature Graph">
                <img src="/static/soil.png" alt="Soil Graph">
                <img src="/static/yield.png" alt="Yield Graph">
                <img src="/static/fertilizer.png" alt="Fertilizer Graph">
                <img src="/static/pesticide.png" alt="Pesticide Graph">
                <img src="/static/combined_graph.png" alt="Combined Graph">
            </div>
        </body>
        </html>
        """
        return html

    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
