"""API Gateway for Temple Analytics microservices"""
from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="Temple Analytics API Gateway")

# Downstream service URLs (environment variables recommended)
MARKET_DATA_URL = "http://market_data_service:8001"
ORDER_SERVICE_URL = "http://order_service:8002"
USER_SERVICE_URL = "http://user_service:8003"
NOTIFY_SERVICE_URL = "http://notification_service:8004"

@app.get("/health")
async def health_check():
    return {"status": "OK", "service": "api_gateway"}

@app.get("/prices/{symbol}")
async def prices(symbol: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{MARKET_DATA_URL}/prices/{symbol}")
        return resp.json()

@app.post("/orders/")
async def create_order(request: Request):
    payload = await request.json()
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{ORDER_SERVICE_URL}/orders", json=payload)
        return resp.json()

@app.get("/profile/{user_id}")
async def get_profile(user_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{USER_SERVICE_URL}/profile/{user_id}")
        return resp.json()