from fastapi import FastAPI
from api import webcam

app = FastAPI()

app.include_router(webcam.router)


@app.get("/")
def index():
    return {"message": "realtime-web-cam-demo"}
