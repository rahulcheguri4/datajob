import csv
import os
import logging
from datetime import datetime


# Folder paths
INPUT_FILE = "data/employees.csv"
OUTPUT_FILE = "output/employee_report.csv"
LOG_FILE = "logs/job.log"


# Create folders if they don't exist
os.makedirs("output", exist_ok=True)
os.makedirs("logs", exist_ok=True)


# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def process_data():

    logging.info("Job started")

    try:

        # Read input CSV
        with open(INPUT_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            employees = list(reader)

        logging.info(f"Read {len(employees)} employee records")

        # Calculate total salary
        total_salary = 0

        for employee in employees:
            total_salary += int(employee["salary"])

        # Calculate average salary
        average_salary = total_salary / len(employees)

        # Create report
        with open(OUTPUT_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Report Date",
                "Total Employees",
                "Total Salary",
                "Average Salary"
            ])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                len(employees),
                total_salary,
                round(average_salary, 2)
            ])

        logging.info("Report generated successfully")
        logging.info(f"Output file: {OUTPUT_FILE}")

    except Exception as error:

        logging.error(f"Job failed: {error}")

        print("Job failed:", error)

        return

    print("Job completed successfully!")


if __name__ == "__main__":
    process_data()
