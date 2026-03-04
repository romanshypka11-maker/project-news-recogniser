from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title = "Fake News Detector API")

detector_model = joblib.load("fake_news_detector.pkl")

class NewRequest(BaseModel):
    query: str

@app.post("/detect")
async def check_news(request: NewRequest):
    prediction = detector_model.predict([request.query])[0]

    if prediction == 0:
        status = "its_fake"
    else:
        status = "its_true"

    return {
        "status": status
    }