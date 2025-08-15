# AllPi
This repo will soon be full with everything Raspberry Pi.
All the code in this repository is solid Python.
The files "Pi-1.py" to "Pi-6.py" are complete, already containing code.

# The Files
The main purpose of this repository is to provide multiple testing and stressing
options you can enter in the Raspberry Pi's terminal to ensure your Pi's stability.
Continue scrolling down to find the "info" for each "Pi" file.

# Info for Pi-1
[12:00:01] CPU: 99.8% | RAM: 86.3% | TEMP: 72.3°C | Time Left: 00:59:58
[12:00:02] CPU: 100.0% | RAM: 88.1% | TEMP: 73.1°C | Time Left: 00:59:57
...

* This section will receive updates*

# Info for Pi-2
The file "at2.py" Maxes out CPU operation,
and verifies thermal stability and performance.

# Info for Pi-3
The file "at3.py"
effortessly tests the 
RAM of your Raspberry Pi.

* This section will receive updates*

# Info for Pi-4
The file "at5.py" simply tests the power consumption (and usage) 
of your Raspberry Pi.
The testing is safe. 
It works by maxing out all of the CPU cores.

# Info for Pi-5
All code is written in Python. 
Important Notes: This only works on some Raspberry Pi models (like Pi 2, 3, and 4).
On some newer Pis, the ACT LED may be handled differently, or unavailable.

1. input = echo none | sudo tee /sys/class/leds/led0/trigger

2. use the file "at5.py"

To restore, input = echo mmc0 | sudo tee /sys/class/leds/led0/trigger
---------------
To run script: 

input = sudo python3 act_led_schedule.py

You need sudo because writing to "/sys/class/leds/..." requires root privileges.
================================================================================

# Info for Pi-6

# About Updates
Updates will take place over time.
Upcoming releases will also 
take place into the near future.
Please be patient. Thank You!

![35% Complete](https://img.shields.io/badge/Progress-35%25-darkred)
