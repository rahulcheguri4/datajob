Scheduled Python Data Job

A simple Python automation project that processes sales data, calculates total and average sales, generates a report, and runs automatically at a scheduled time interval.

📌 Project Overview

The Scheduled Python Data Job demonstrates how to automate a data-processing task using Python.

The program:

Stores sample sales data
Calculates total sales
Calculates average sales
Generates a report.txt file
Runs automatically using the schedule library
Can be extended with logging and error handling
🛠️ Technologies Used
Python
Schedule Python Library
File Handling
Datetime
📂 Project Structure
PythonDataJob/
│
├── main.py
├── report.txt
└── job.log
⚙️ Requirements

Make sure Python is installed.

Check the Python version:

python --version

Install the required library:

pip install schedule
🚀 How to Run
1. Clone or download the project

Open the project folder in VS Code.

2. Install the dependency
pip install schedule
3. Run the Python program
python main.py

You should see:

Scheduler started...
The job will run every 10 seconds.

After 10 seconds, the job runs automatically.

📊 Sample Output
-----------------------------
Python Data Job Started
-----------------------------
Total Sales   : 10000
Average Sales : 2000.0
Report created successfully!
Job completed.
📄 Generated Report

The program creates a report.txt file:

SALES REPORT
--------------------
Date: 2026-09-08 16:00:00
Total Sales: 10000
Average Sales: 2000.0
⏰ Scheduling

The project currently runs the job every 10 seconds:

schedule.every(10).seconds.do(data_job)

You can change it to every minute:

schedule.every(1).minutes.do(data_job)

Every hour:

schedule.every(1).hours.do(data_job)

Every day at 9:00 AM:

schedule.every().day.at("09:00").do(data_job)
🔄 How the Project Works
Start Program
     ↓
Scheduler Starts
     ↓
Wait for Scheduled Time
     ↓
Run Data Job
     ↓
Process Sales Data
     ↓
Calculate Total Sales
     ↓
Calculate Average Sales
     ↓
Generate Report
     ↓
Save report.txt
     ↓
Wait for Next Schedule
     ↓
Repeat
🎯 Learning Objectives

Through this project, you can learn:

Python functions
Lists and calculations
File handling
Creating reports
Python modules
Date and time handling
Task scheduling
Basic automation
🔮 Future Improvements

This project can be upgraded by adding:

CSV dataset processing
API data retrieval
Database connectivity
Error handling
Execution logging
Email notifications
Daily automated reports
Windows Task Scheduler
Cloud deployment
