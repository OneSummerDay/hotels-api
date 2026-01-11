from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/hotels")
def get_hotels(
    location,
    date_from, 
    date_to,
    stars: Optional[int] = None,
    has_spa: Optional[bool] = None,
):
    return  date_from, date_to