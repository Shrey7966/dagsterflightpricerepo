from dagster import Definitions
from my_dagster_project.my_dag import flight_price_collection, daily_schedule  # Import job and schedule

defs = Definitions(
    jobs=[flight_price_collection],  # List your jobs
    schedules=[daily_schedule],  # List your schedules
)
