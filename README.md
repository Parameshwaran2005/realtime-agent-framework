# Banking Intent Classifier API

A 77-class intent classifier for real-time banking query routing, built on the Banking77 dataset. Uses TF-IDF vectorization + Logistic Regression, deployed as a FastAPI REST API.

## Setup
pip install -r requirements.txt

## Run
uvicorn app:app --reload

## Usage
POST /predict
{
  "text": "I lost my card, what should I do?"
}

Response:
{
  "query": "I lost my card, what should I do?",
  "predicted_intent": "lost_or_stolen_card",
  "confidence": 0.87
}

## Model
- Vectorizer: TF-IDF (unigrams + bigrams, 5000 max features)
- Classifier: Logistic Regression
- Dataset: Banking77 (77 intents, ~10k training queries)# Banking Intent Classifier API

A 77-class intent classifier for real-time banking query routing, built on the Banking77 dataset. Uses TF-IDF vectorization + Logistic Regression, deployed as a FastAPI REST API.

## Setup
pip install -r requirements.txt

## Run
uvicorn app:app --reload

## Usage
POST /predict
{
  "text": "I lost my card, what should I do?"
}

Response:
{
  "query": "I lost my card, what should I do?",
  "predicted_intent": "lost_or_stolen_card",
  "confidence": 0.87
}

## Model
- Vectorizer: TF-IDF (unigrams + bigrams, 5000 max features)
- Classifier: Logistic Regression
- Dataset: Banking77 (77 intents, ~10k training queries)