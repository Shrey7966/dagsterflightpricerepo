from dagster import Definitions
from my_dag import flight_price_collection, daily_flight_price_collection  # Import your job and schedule

# This is where you define all your jobs, schedules, and sensors
defs = Definitions(
    jobs=[flight_price_collection],  # List your jobs
    schedules=[daily_flight_price_collection],  # List your schedules
)
