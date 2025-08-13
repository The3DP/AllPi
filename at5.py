import time
from datetime import datetime, timedelta

ACT_LED_PATH = "/sys/class/leds/led0/brightness"

def set_led(state: bool):
    with open(ACT_LED_PATH, 'w') as f:
        f.write('1' if state else '0')

print("Starting ACT LED timer (20 min ON per hour)...")

try:
    while True:
        now = datetime.now()
        start_of_hour = now.replace(minute=0, second=0, microsecond=0)
        next_hour = start_of_hour + timedelta(hours=1)
        on_until = start_of_hour + timedelta(minutes=20)

        if now < on_until:
            # Turn LED ON
            set_led(True)
            time.sleep((on_until - now).total_seconds())
        else:
            # Turn LED OFF
            set_led(False)
            time.sleep((next_hour - now).total_seconds())
except KeyboardInterrupt:
    print("\nRestoring default ACT LED behavior...")
    # Reset ACT LED to default trigger (SD activity)
    with open("/sys/class/leds/led0/trigger", 'w') as f:
        f.write('mmc0')
      
