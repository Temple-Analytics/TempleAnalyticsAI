"""Market Data Service for fetching and aggregating price data"""
from fastapi import FastAPI
import random

app = FastAPI(title="Market Data Service")

@app.get("/prices/{symbol}")
def get_price(symbol: str):
    # Simulate price retrieval from CEX and DEX
    price = round(random.uniform(20, 200), 2)
    return {"symbol": symbol, "price": price, "source": "simulated"}

@app.get("/orderbook/{symbol}")
def get_orderbook(symbol: str):
    # Simulate orderbook data
    bids = [[round(random.uniform(20, 100), 2), random.randint(1, 50)] for _ in range(5)]
    asks = [[round(random.uniform(100, 200), 2), random.randint(1, 50)] for _ in range(5)]
    return {"symbol": symbol, "bids": bids, "asks": asks}