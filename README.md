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

![50% Complete](https://img.shields.io/badge/Progress-50%25-darkred)
