from fastapi import FastAPI
from api import webcam

app = FastAPI()

app.include_router(webcam.router)
