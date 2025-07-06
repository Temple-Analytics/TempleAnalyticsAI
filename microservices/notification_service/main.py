"""Notification Service for sending alerts"""
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI(title="Notification Service")

class Alert(BaseModel):
    user_id: str
    message: str

@app.post("/alerts")
def send_alert(alert: Alert, background_tasks: BackgroundTasks):
    # Simulate sending notification
    background_tasks.add_task(lambda: print(f"Alert for {alert.user_id}: {alert.message}"))
    return {"status": "queued", "user_id": alert.user_id, "message": alert.message}