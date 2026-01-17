from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings", 
    tags=["Bookings"]
)

@router.get("/")
def get_bookings():
    pass


@router.get("/{booking_id}")
def get_booking_by_id(booking_id: int):
    pass