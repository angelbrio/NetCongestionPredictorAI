from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from modelo_loader import modelo

app = FastAPI()

# Define aquí las variables que espera tu modelo
class DatosEntrada(BaseModel):
    variable1: float
    variable2: float
    variable3: float
    # Agrega más si las hay

@app.post("/predecir")
def predecir(datos: DatosEntrada):
    df = pd.DataFrame([datos.dict()])
    pred = modelo.predict(df)
    return {"congestion": bool(pred[0])}
