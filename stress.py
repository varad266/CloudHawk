import multiprocessing

def cpu_stress():
    while True:
        pass  # Infinite loop to consume CPU

# Start multiple CPU-intensive processes
if __name__ == "__main__":
    for _ in range(multiprocessing.cpu_count()):  # Use all CPU cores
        multiprocessing.Process(target=cpu_stress).start()
