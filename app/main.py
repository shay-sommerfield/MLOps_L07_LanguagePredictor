from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from .model.model import predict_pipeline
from .model.model import __version__ as model_version

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Language(BaseModel):
	Input_Lang:str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict")
def predict(payload: Language):
    text = payload.Input_Lang
    return {"Predicted Language": predict_pipeline(text=text)}


