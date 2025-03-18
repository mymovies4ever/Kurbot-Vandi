import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# FastAPI app
app = FastAPI()

# Function to fetch vehicle details
def get_vehicle_info(request_id):
    url = "https://vehicle-rc-verification-advanced.p.rapidapi.com/v3/tasks"
    headers = {
        "X-Rapidapi-Key": RAPIDAPI_KEY,
        "X-Rapidapi-Host": "vehicle-rc-verification-advanced.p.rapidapi.com"
    }
    params = {"request_id": request_id}

    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}

# Endpoint for vehicle search
@app.get("/")
def home():
    return {"message": "Vehicle RC Bot is running!"}

@app.get("/vehicle/{request_id}")
def fetch_vehicle(request_id: str):
    return get_vehicle_info(request_id)
