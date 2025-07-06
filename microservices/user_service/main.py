"""User Profile Service for managing user data"""
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="User Service")

class Profile(BaseModel):
    user_id: str
    total_assets: float
    pnl_1d: float
    pnl_7d: float

@app.get("/profile/{user_id}")
def get_profile(user_id: str):
    # Simulate profile data
    profile = Profile(
        user_id=user_id,
        total_assets=round(random.uniform(1000, 10000), 2),
        pnl_1d=round(random.uniform(-100, 100), 2),
        pnl_7d=round(random.uniform(-500, 500), 2)
    )
    return profile.dict()