import joblib
import os

# Cargar el modelo una sola vez
modelo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "modelo_entrenado.pkl"))
modelo = joblib.load(modelo_path)
