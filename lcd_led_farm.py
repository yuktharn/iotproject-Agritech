import random
import time
from gpiozero import LED
from RPLCD.i2c import CharLCD

dry_led = LED(17)

lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,
    port=1,
    cols=16,
    rows=2
)

soil = 60
tank = 80

while True:
    soil += random.randint(-8, 4)
    soil = max(20, min(90, soil))

    tank += random.randint(-2, 0)
    tank = max(0, tank)

    print(f"Soil={soil}, Tank={tank}")

    # one single condition for everything
    if soil < 40 and tank > 10:
        sprinkler = True
    else:
        sprinkler = False

    # LED follows sprinkler exactly
    if sprinkler:
        dry_led.on()
    else:
        dry_led.off()

    lcd.clear()

    if sprinkler:
        lcd.write_string("SOIL DRY\nSPRINKLER ON")
        print("Sprinkler ON")
        print("LED ON")
    else:
        lcd.write_string("SOIL OK\nSPRINKLER OFF")
        print("Sprinkler OFF")
        print("LED OFF")

    print("------------------")
    time.sleep(5)
