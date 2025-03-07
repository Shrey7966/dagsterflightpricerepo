from dagster import job, op, schedule
import requests
import json
import boto3
from datetime import datetime

# Function to call API and save response
API_KEY = "fdcf5105b0mshb60125cb25ee57ep1565acjsndd740fc93e14"

@op
def fetch_flight_prices():
    url = "https://flights-sky.p.rapidapi.com/flights/search-one-way"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "flights-sky.p.rapidapi.com"
    }
    params = {
        "fromEntityId": "BLR",
        "toEntityId": "JFK",
        "departDate": datetime.today().strftime('%Y-%m-%d'),
        "currency": "INR",
        "cabinClass": "economy"
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    # Save JSON response to S3
    s3_bucket = "flightpricedataanalysis"
    s3_key = f"flight_prices/{datetime.today().strftime('%Y-%m-%d')}/flight_data_test.json"
    
    s3 = boto3.client("s3")
    s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=json.dumps(data))
    print(f"Saved data to s3://{s3_bucket}/{s3_key}")

@job
def flight_price_collection():
    fetch_flight_prices()
    
daily_schedule = dg.ScheduleDefinition(
    job=flight_price_collection,
    cron_schedule="0 0 * * *",  # Runs at midnight daily
)
