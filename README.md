# PythonProgramAssessment

# Pre-requisites

1. Install Python3.x in Windows
2. Install Visual Studio Code

# Program - SystemHealthMonitor

1. In VS code, open Terminal and run the command `pip install psutil`
2. Run the program using the command `python systemHealthMonitor.py`

# Description - SystemHealthMonitor

1. The program verifies the health of a linux system and checks the following against predefined threshold of 80%:

   1. CPU usage
   2. Memory usage
   3. Disk space
   4. Running processes
   If any of these is greater than 80%, shows message in the console as well as updates the log
2. The logs are stored in `system_health.log`

# Program - ApplicationHealthCheck

1. In VS code open Terminal and run the command `pip install requests`
2. Run the program using the command `python applicationHealthCheck.py`

# Description - ApplicationHealthCheck

1. The program verifies the UP time using the requests library. It would display appropriate messages when the application is up or down.
2. The logs are stored in `app_health.log`
