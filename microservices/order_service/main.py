"""Order Execution Service for placing and managing orders"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI(title="Order Service")

class Order(BaseModel):
    symbol: str
    side: str
    quantity: float
    price: float = None  # Optional for market orders

orders_db = {}

@app.post("/orders")
def place_order(order: Order):
    order_id = str(uuid.uuid4())
    orders_db[order_id] = order.dict()
    return {"order_id": order_id, "status": "filled", **order.dict()}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]