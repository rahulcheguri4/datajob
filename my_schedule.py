import my_schedule
import time
import logging

from data_job import process_data


logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_job():

    logging.info("Scheduled job triggered")

    try:
        process_data()
        logging.info("Scheduled job completed")

    except Exception as error:
        logging.error(f"Scheduled job failed: {error}")


print("Scheduler started...")
print("Job will run every 10 seconds.")
