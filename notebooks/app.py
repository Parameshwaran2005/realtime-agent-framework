from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="Banking Intent Classifier API")

# Load model + vectorizer once at startup
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


class Query(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Banking Intent Classifier is running"}


@app.post("/predict")
def predict_intent(query: Query):
    vec = vectorizer.transform([query.text])
    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    confidence = float(probabilities.max())

    return {
        "query": query.text,
        "predicted_intent": prediction,
        "confidence": round(confidence, 4)
    }