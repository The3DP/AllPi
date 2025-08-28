import time
import psutil
from datetime import datetime
from board import SCL, SDA
import busio
from adafruit_ina219 import INA219

# ACT LED control path
ACT_LED_BRIGHTNESS = "/sys/class/leds/led0/brightness"
ACT_LED_TRIGGER = "/sys/class/leds/led0/trigger"

# Function to control ACT LED
def set_act_led(state: bool):
    try:
        with open(ACT_LED_BRIGHTNESS, 'w') as f:
            f.write('1' if state else '0')
    except Exception as e:
        print(f"Failed to set ACT LED: {e}")

# Set ACT LED to manual control
with open(ACT_LED_TRIGGER, 'w') as f:
    f.write('none')

# Set up INA219 sensor
i2c_bus = busio.I2C(SCL, SDA)
ina = INA219(i2c_bus)

print("Monitoring power and CPU...")

try:
    while True:
        # Read power usage in watts
        try:
            power = ina.power  # in milliwatts
            watts = power / 1000.0
        except Exception as e:
            print(f"INA219 read error: {e}")
            watts = 0.0

        # Read CPU stats
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_temp = psutil.sensors_temperatures().get("cpu-thermal", [{}])[0].get("current", "N/A")

        print(f"{datetime.now()} | Power: {watts:.2f} W | CPU Load: {cpu_percent:.1f}% | CPU Temp: {cpu_temp}°C")

        # Control ACT LED based on power threshold
        if watts < 12.0:
            set_act_led(True)
        else:
            set_act_led(False)

        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting and restoring ACT LED default trigger...")
    with open(ACT_LED_TRIGGER, 'w') as f:
        f.write('mmc0')
