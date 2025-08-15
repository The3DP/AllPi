import multiprocessing as mp
import numpy as np
import time
import os
import psutil
import threading
import pygame
import random
from datetime import datetime, timedelta

# CONFIG
TEST_DURATION = 60 * 60  # 1 hour in seconds
TEMP_FOLDER = "/tmp/pi_stress_test"
CPU_THREADS = os.cpu_count()
RAM_USAGE_MB = 300  # per RAM thread
DISK_FILE_SIZE_MB = 200  # per file
DISK_FILES = 10

# Ensure temp folder exists
os.makedirs(TEMP_FOLDER, exist_ok=True)


def stress_cpu(core_id):
    while True:
        np.linalg.eig(np.random.rand(300, 300))


def stress_ram():
    arrays = []
    for _ in range(int(RAM_USAGE_MB / 50)):
        arr = np.random.rand(6250000)  # ~50 MB
        arrays.append(arr)
    while True:
        _ = [np.sum(arr) for arr in arrays]


def stress_disk():
    while True:
        for i in range(DISK_FILES):
            file_path = f"{TEMP_FOLDER}/testfile_{i}.bin"
            with open(file_path, "wb") as f:
                f.write(os.urandom(DISK_FILE_SIZE_MB * 1024 * 1024))
            with open(file_path, "rb") as f:
                _ = f.read()


def stress_gpu():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    start = time.time()

    while running and (time.time() - start < TEST_DURATION):
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for _ in range(1000):
            pygame.draw.circle(screen, (255, 255, 255),
                               (random.randint(0, 800), random.randint(0, 600)),
                               random.randint(1, 10))
        pygame.display.flip()
        clock.tick(60)


def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        for name in temps:
            for entry in temps[name]:
                if "cpu" in entry.label.lower() or "core" in entry.label.lower():
                    return entry.current
        # Fallback to vcgencmd
        res = os.popen("vcgencmd measure_temp").read()
        if "temp=" in res:
            return float(res.strip().split('=')[1].replace("'C", ""))
    except:
        pass
    return None


def monitor(start_time, end_time):
    print("Monitoring started.")
    while True:
        now = datetime.now()
        if now >= end_time:
            break
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        temp = get_cpu_temp()
        remaining = end_time - now
        time_str = str(remaining).split('.')[0]  # clean HH:MM:SS format
        print(f"[{now.strftime('%H:%M:%S')}] CPU: {cpu:5.1f}% | RAM: {mem.percent:5.1f}% | TEMP: {temp or 'N/A'}°C | Time Left: {time_str}")
        time.sleep(1)


if __name__ == "__main__":
    print("=== Raspberry Pi 4B Stress Test ===")
    print(f"🕒 Duration: {TEST_DURATION // 60} minutes")
    print(f"💥 Using {CPU_THREADS} CPU cores, RAM, Disk, and GPU")
    print("🚀 Starting in 3 seconds... (CTRL+C to abort)")
    time.sleep(3)

    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=TEST_DURATION)

    # Start CPU stress
    cpu_processes = [mp.Process(target=stress_cpu, args=(i,)) for i in range(CPU_THREADS)]
    for p in cpu_processes:
        p.start()

    # Start RAM stress
    ram_processes = [mp.Process(target=stress_ram) for _ in range(2)]
    for p in ram_processes:
        p.start()

    # Start Disk stress
    disk_thread = threading.Thread(target=stress_disk)
    disk_thread.start()

    # Start GPU stress
    gpu_thread = threading.Thread(target=stress_gpu)
    gpu_thread.start()

    # Start monitor
    monitor_thread = threading.Thread(target=monitor, args=(start_time, end_time))
    monitor_thread.start()

    # Wait for full duration
    time.sleep(TEST_DURATION)

    # Cleanup
    print("\n⏱️ Test complete. Cleaning up...")
    for p in cpu_processes + ram_processes:
        p.terminate()
    disk_thread.join(timeout=1)
    gpu_thread.join(timeout=1)
    monitor_thread.join(timeout=1)
    pygame.quit()

    # Remove disk files
    try:
        for i in range(DISK_FILES):
            os.remove(f"{TEMP_FOLDER}/testfile_{i}.bin")
        os.rmdir(TEMP_FOLDER)
    except Exception:
        pass

    print("✅ Cleanup complete. Stress test finished successfully.")
