from sqlalchemy import select
from fastapi import APIRouter

from app.bookings.models import Booking
from app.database import async_session_maker


router = APIRouter(
    prefix="/bookings", 
    tags=["Bookings"]
)

@router.get("/")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Booking)
        result = await session.execute(query)
        bookings = result.fetchall()
        return bookings