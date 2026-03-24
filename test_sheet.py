import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time
from datetime import datetime

print("Step 1: Program started")

KEY_FILE = "smart_key.json"
SPREADSHEET_KEY = "1shO5FPKr9zkNdrNju_QAOk4TOVF-CHnKNV2uLA1qTzA"

print("Step 2: Setting scope")
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

print("Step 3: Loading credentials")
creds = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, scope)

print("Step 4: Authorizing client")
client = gspread.authorize(creds)

print("Step 5: Opening Google Sheet by key")
sheet = client.open_by_key(SPREADSHEET_KEY).sheet1

print("Step 6: Connected successfully")

soil = 60
tank = 80

while True:
    temp = random.randint(25, 35)
    humidity = random.randint(50, 85)

    soil += random.randint(-3, 3)
    soil = max(20, min(90, soil))

    tank += random.randint(-2, 0)
    tank = max(0, tank)

    flow = round(random.uniform(0, 2), 2)

    stress = 0
    if soil < 35 or soil > 85:
        stress += 1
    if temp > 33:
        stress += 1
    if humidity > 80:
        stress += 1

    fertilizer = 3
    if soil < 40:
        fertilizer += 2
    if temp > 33:
        fertilizer += 1

    pesticide = 2
    if humidity > 80:
        pesticide += 3
    if soil > 70:
        pesticide += 2

    yield_score = 100 - stress * 10
    now = datetime.now().strftime("%H:%M:%S")

    row = [
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
    ]

    print("Step 7: Sending row...", row)
    sheet.append_row(row)
    print("Step 8: Row sent successfully")

    time.sleep(10)
