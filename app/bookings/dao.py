from app.database import async_session_maker
from app.bookings.models import Booking
from sqlalchemy import select



class BookingDAO:
    
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Booking)
            result = await session.execute(query)
            bookings = result.fetchall()
            return bookings
