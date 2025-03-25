from dagster import Definitions
from my_dagster_project.flight_price_collection_job import flight_price_collection, daily_schedule  # Import job and schedule

defs = Definitions(
    jobs=[flight_price_collection],  # List your jobs
    schedules=[daily_schedule],  # List your schedules
)
