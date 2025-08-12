import multiprocessing
import time

def burn():
    while True:
        pass  # Infinite loop to keep the CPU core busy

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Starting {num_cores} CPU stress processes...")
    
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=burn)
        p.start()
        processes.append(p)
    
    try:
        while True:
            time.sleep(1)  # Keep main thread alive
    except KeyboardInterrupt:
        print("\nStopping stress test...")
        for p in processes:
            p.terminate()
            p.join()
