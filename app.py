# import joblib
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# import numpy as np

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # تحميل النموذج
# model = joblib.load("xgboost_iris_model.joblib")

# # تعريف نموذج البيانات
# class IrisFeatures(BaseModel):
#     sepal_length: float
#     sepal_width: float
#     petal_length: float
#     petal_width: float

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/predict")
# async def predict(iris: IrisFeatures):
#     features = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
#     prediction = model.predict(features)
#     return {"prediction": prediction[0]}

# ==============================



from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib

app = FastAPI()

# تحميل النموذج
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
    prediction = model.predict(data)[0]  # احصل على القيمة مباشرة
    
    species = {0: "Iris Setosa", 1: "Iris Versicolor", 2: "Iris Virginica"}
    predicted_species = species.get(prediction, "Unknown species")

    return {"prediction": predicted_species}

