import psutil
import time

# Define thresholds
CPU_THRESHOLD = 80 
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80   
PROCESS_THRESHOLD = 100 

print("Execution Started")

while True:
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print("Alert: CPU usage exceeds threshold")

    # Check memory usage
    memory_usage = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        print("Alert: Memory usage exceeds threshold")

    # Check disk usage
    disk_usage = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        print("Alert: Disk usage exceeds threshold")

    # Check running processes
    num_processes = len(psutil.pids())
    print(f"Number of Processes: {num_processes}")
    if num_processes > PROCESS_THRESHOLD:
        print("Alert: Too many processes running")

    print("Execution finished")

    # Wait for 2 seconds before the next iteration
    time.sleep(2)
