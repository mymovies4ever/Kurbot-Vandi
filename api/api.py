import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Key
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

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}

# API Routes
@app.get("/")
def home():
    return {"message": "Vehicle RC Bot is running!"}

@app.get("/vehicle/{request_id}")
def fetch_vehicle(request_id: str):
    if not request_id:
        raise HTTPException(status_code=400, detail="Request ID is required")
    
    data = get_vehicle_info(request_id)
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    
    return data
