# 🧠 AllPi – The Ultimate Raspberry Pi Testing Hub

Welcome to **AllPi**, a growing suite of **Python-based tools** designed to test, stress, and monitor your Raspberry Pi. Whether you're benchmarking performance, verifying thermal stability, or measuring power usage, AllPi has you covered — right from the terminal.

AllPi is written in solid, clean Python and fully optimized for Raspberry Pi models 2, 3, and 4 (with limited support for newer models).

> ⚙️ Files `Pi-1.py` to `Pi-6.py` are complete and ready to run.

---

## 📂 Repository Purpose

The goal of this repository is to provide **multiple, real-world testing and stress options** you can run directly on your Raspberry Pi. These tests help ensure your system’s **reliability, thermal performance, and hardware behavior** under load.

Keep reading for details on each file!

---

## 📄 File Overview

| File        | Purpose                                       |
|-------------|-----------------------------------------------|
| `Pi-1.py`   | General system stress with real-time stats    |
| `Pi-2.py`   | Maxes CPU load for thermal stability testing  |
| `Pi-3.py`   | Tests and stresses RAM memory                 |
| `Pi-4.py`   | Power usage test via CPU stress               |
| `Pi-5.py`   | Controls ACT LED (limited to supported models)|
| `Pi-6.py`   | Measures power in watts using external sensor |

---

## 🧪 Pi-1: System Stress Monitor

This script applies a moderate stress test and outputs real-time stats like:

[12:00:01] CPU: 99.8% | RAM: 86.3% | TEMP: 72.3°C | Time Left: 00:59:58
[12:00:02] CPU: 100.0% | RAM: 88.1% | TEMP: 73.1°C | Time Left: 00:59:57


🔄 This section will receive additional features in future updates.

---

## 🔥 Pi-2: Max CPU Load & Thermal Test

**`Pi-2.py`** is designed to **fully load your CPU**, pushing your Pi to maximum operating temperatures. It's ideal for **thermal stability testing**.

---

## 🧠 Pi-3: RAM Stress Test

**`Pi-3.py`** efficiently tests **RAM stability** using high memory operations to verify your Pi’s memory subsystem is functioning correctly.

🔄 More features are on the way!

---

## ⚡ Pi-4: CPU Power Usage Estimator

**`Pi-4.py`** simulates high CPU power draw by maxing out all cores.  
While it doesn’t measure power directly, it's useful for:

- Power draw estimation
- Cooling effectiveness testing

✅ Safe for all models.

---

## 💡 Pi-5: ACT LED Control (Model Dependent)

This script allows you to control the onboard **ACT LED**.  
**Only works on models where the LED is accessible via `/sys/class/leds/led0`**.

### 🧰 Steps

1. Disable default ACT LED behavior:
   ```bash
   echo none | sudo tee /sys/class/leds/led0/trigger



![50% Complete](https://img.shields.io/badge/Progress-50%25-darkred)
