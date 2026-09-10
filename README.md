# Automated-Platform-Surveillance
# Platform Surveillance System

A Python-based automation tool for monitoring system resources and running processes. The program periodically collects CPU, RAM, network, and process information and stores the details in timestamped log files.

## Features

- Monitors CPU usage and active CPU cores.
- Monitors RAM usage and total RAM.
- Tracks network data sent and received.
- Scans currently running processes.
- Records process ID (PID), name, username, and status.
- Records CPU and memory usage of processes.
- Automatically creates a log directory if it does not exist.
- Generates timestamped log files.
- Supports periodic execution using a scheduler.
- Provides command-line help and usage options.

## Technologies Used

- Python
- Psutil
- Schedule
- OS Module
- Sys Module
- Time Module

## How to Run

Run the program using:

```bash
python AutomatedPlatformSurveillance.py Time_Interval Folder_Name
