import numpy as np
import time

def stress_cpu(duration=30):
    print("Stressing CPU...")
    end = time.time() + duration
    while time.time() < end:
        np.linalg.eig(np.random.rand(300, 300))
    print("CPU stress test complete.")

stress_cpu()
