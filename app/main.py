from fastapi import FastAPI, Query
from typing import Optional
from datetime import date

from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    name: str
    location: str
    stars: int
    has_spa: bool

@app.get("/hotels", response_model=list[SHotel])
def get_hotels(
    location: str,
    date_from: date, 
    date_to: date,
    stars: Optional[int] = Query(None, ge=1, le=5),
    has_spa: Optional[bool] = None,
):
    hotels = [
        {
            "name": "Hotel Sunshine",
            "location": "Beach City",
            "stars": 4,
            "has_spa": True
        },
        {
            "name": "Mountain Retreat",
            "location": "Hill Town",
            "stars": 5,
            "has_spa": False
        }
    ]
    return  hotels


class SBooking(BaseModel):
    hotel_id: int
    date_from: date
    date_to: date

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass