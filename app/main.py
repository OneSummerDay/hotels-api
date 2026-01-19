from fastapi import Depends, FastAPI, Query
from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.bookings.router import router as bookings_router
from app.users.router import register_user

app = FastAPI()

app.include_router(register_user)
app.include_router(bookings_router)


class HotelsSearchArgs():
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa

class SHotel(BaseModel):
    name: str
    location: str
    stars: int
    has_spa: bool

@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
) -> list[SHotel]:
    return  search_args


class SBooking(BaseModel):
    hotel_id: int
    date_from: date
    date_to: date

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass