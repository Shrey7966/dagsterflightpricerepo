from dagster import Definitions
from my_dag import flight_price_collection, daily_schedule  # Corrected import for the schedule

# This is where you define all your jobs, schedules, and sensors
defs = Definitions(
    jobs=[flight_price_collection],  # List your jobs
    schedules=[daily_schedule],  # List your schedules
)
