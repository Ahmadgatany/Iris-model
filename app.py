from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("xgboost_iris_model.joblib")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/predict")
async def predict(input_data: IrisInput):
    data = [[input_data.sepal_length, input_data.sepal_width, input_data.petal_length, input_data.petal_width]]
    prediction = model.predict(data)[0] 
    
    species = {0: "Iris Setosa", 1: "Iris Versicolor", 2: "Iris Virginica"}
    predicted_species = species.get(prediction, "Unknown species")

    return {"prediction": predicted_species}

