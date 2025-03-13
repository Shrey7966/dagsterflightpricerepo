from dagster import job, op
import requests
import json
import boto3
from datetime import datetime,timedelta
import dagster as dg  # Correctly importing Dagster with alias 'dg'


# Function to call API and save response
API_KEY = "fdcf5105b0mshb60125cb25ee57ep1565acjsndd740fc93e14"

@op
def fetch_flight_prices():
    url = "https://flights-sky.p.rapidapi.com/flights/search-one-way"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "flights-sky.p.rapidapi.com"
    }
    
    # Fetch date (when we are collecting data)
    fetch_date = datetime.today().strftime('%Y-%m-%d')

    # Depart date (when the flight is scheduled)
    depart_date = "2025-03-28"

    params = {
        "fromEntityId": "BLR",
        "toEntityId": "JFK",
        "departDate": depart_date,
        "currency": "INR",
        "cabinClass": "economy",
        "stops":"direct,1stop,2stops"
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    # Save JSON response to S3
    s3_bucket = "flightpriceanalysisproject"
    s3_key = f"flight_prices/{fetch_date}/{depart_date}.json" # New path format
    
    s3 = boto3.client("s3")
    s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=json.dumps(data))
    
    print(f"✅ Saved data to s3://{s3_bucket}/{s3_key}")

@job
def flight_price_collection():
    fetch_flight_prices()

# Using dg.ScheduleDefinition correctly
daily_schedule = dg.ScheduleDefinition(
    job=flight_price_collection,
    cron_schedule="0 0 * * *",  # Runs at midnight daily
)
