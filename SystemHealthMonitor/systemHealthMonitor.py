import psutil
import time
import logging


logging.basicConfig(filename="SHM\system_health.log", 
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 90  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f"High CPU Usage detected: {cpu_usage}%"
        print(message)
        logging.warning(message)
    else:
        print(f"CPU Usage: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        message = f"High Memory Usage detected: {memory_usage}%"
        print(message)
        logging.warning(message)
    else:
        print(f"Memory Usage: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    if disk_percent > DISK_THRESHOLD:
        message = f"High Disk Usage detected: {disk_percent}%"
        print(message)
        logging.warning(message)
    else:
        print(f"Disk Usage: {disk_percent}%")

def check_running_processes():
    process_count = len(psutil.pids())
    print(f"Number of running processes: {process_count}")
    
    logging.info(f"Running processes count: {process_count}")

def monitor_system_health():
    print("Monitoring system health...\n")
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        print("-" * 50)
        
        
        time.sleep(5)

if __name__ == "__main__":
    try:
        monitor_system_health()
    except KeyboardInterrupt:
        print("System Health Monitoring stopped.")
