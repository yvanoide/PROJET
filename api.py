from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel
import pickle
from fastapi import FastAPI, File, UploadFile
import numpy as np 
from pydantic import BaseModel
import pickle
import pandas as pd

import mlflow
import os
import boto3

# Création des tags
tags = [
       {
              "name": "Hello",
              "description": "Hello World",
       },
       {
              "name": "Predict",
              "description": "Predict",
       },
]
 
# Créez l'application FastAPI
app = FastAPI(
    title="API de prédiction",
    description="Prédictions",
    version="1.0.0",
    openapi_tags=tags,
)

# Point de terminaison avec paramètre
@app.get("/hello", tags=["Hello name V1"])
def hello(name: str='World'):
        return {"message": f"Hello {name}"}


 
# Chargez les modèles au démarrage pour l'efficacité (considérez le caching pour les grands modèles)
try:
    with open("model_1.pkl", "rb") as f:
        model_1 = pickle.load(f)
    with open("model_2.pkl", "rb") as f:
        model_2 = pickle.load(f)
except FileNotFoundError as e:
    print(f"Erreur lors du chargement des modèles : {e}")
    raise

# Définissez les modèles de données pour la validation et la clarté
class Credit(BaseModel):
    Gender: int
    Age: int
    Physical_Activity_Level: int
    Heart_Rate: int
    Daily_Steps: int
    BloodPressure_high: int
    BloodPressure_low: int

class Health(BaseModel):
    Physical_Activity_Level: int
    Heart_Rate: int
    Daily_Steps: int
    Sleep_Disorder: int

@app.post("/predict", tags=["Prédiction V1"])
async def predict_model1(credit: Credit = Body(...)):
    try:
        data = [[credit.Gender, credit.Age, credit.Physical_Activity_Level, credit.Heart_Rate, credit.Daily_Steps, credit.BloodPressure_high, credit.BloodPressure_low]]
        prediction = model_1.predict(data)[0]  # En supposant que cela renvoie une seule prédiction
        return {"prediction": int(prediction)}  # Convertir la prédiction en type natif Python
    except Exception as e:
        return {"error": str(e)}

# Point de terminaison pour le Modèle 2
@app.post("/predict2", tags=["Prédiction V2"])
async def predict_model2(health: Health = Body(...)):
    try:
        data = [[health.Physical_Activity_Level, health.Heart_Rate, health.Daily_Steps, health.Sleep_Disorder]]
        prediction = model_2.predict(data)[0]  # En supposant que cela renvoie une seule prédiction
        return {"prediction": int(prediction)}  # Convertir la prédiction en type natif Python
    except Exception as e:
        return {"error": str(e)}

# Lancez le serveur 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
