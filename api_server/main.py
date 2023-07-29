from fastapi import FastAPI
from api import webcam
from util.error_handling import CustomException, unvicorn_exception_handelr

app = FastAPI()

app.include_router(webcam.router)
app.add_exception_handler(CustomException, unvicorn_exception_handelr)


@app.get("/")
def index():
    return {"message": "realtime-web-cam-demo"}
