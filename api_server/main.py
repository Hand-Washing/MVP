# pakages
from fastapi import FastAPI

# module
from api import webcam
from util.error_handling import CustomException, video_exception_handelr


app = FastAPI()
app.include_router(webcam.router)
app.add_exception_handler(CustomException, video_exception_handelr)


# endpoint
@app.get("/")
def index():
    return {"message": "realtime-web-cam-demo"}
