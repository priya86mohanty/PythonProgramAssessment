import requests
import time
import logging

app_url = "https://www.amazon.in/"  

logging.basicConfig(filename="ApplicationHealthCheck\\app_health.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def check_application_status():
    try:
        response = requests.get(app_url, timeout=5)
        
        if response.status_code == 200:
            status_message = f"Application is UP (Status Code: {response.status_code})"
            print(status_message)
            logging.info(status_message)
        else:
            status_message = f"Application might be DOWN (Status Code: {response.status_code})"
            print(status_message)
            logging.warning(status_message)
    except requests.ConnectionError:
        status_message = "Application is DOWN (Failed to connect)"
        print(status_message)
        logging.error(status_message)
    except requests.Timeout:
        status_message = "Application is DOWN (Request Timed Out)"
        print(status_message)
        logging.error(status_message)


def monitor_application(interval=60):
    print(f"Starting to monitor the application health at {app_url}\n")
    while True:
        check_application_status()
        time.sleep(interval)  

if __name__ == "__main__":
    try:
        monitor_application(interval=60)  
    except KeyboardInterrupt:
        print("Application Health Monitoring stopped.")
