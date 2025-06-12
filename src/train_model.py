# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# 1. Construir la ruta absoluta del archivo CSV
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "datos_red.csv"))

# 2. Cargar los datos con separador de punto y coma (;)
df = pd.read_csv(data_path, sep=";", decimal=",")

# 3. Verificar columnas
print("Columnas del archivo:")
print(df.columns.tolist())

# 4. Normalizar nombres (opcional pero recomendado)
df.columns = df.columns.str.strip().str.lower()

# 5. Separar variables predictoras (X) y variable objetivo (y)
X = df.drop(columns=["tiempo", "congestion"])
y = df["congestion"]

# 6. Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 8. Evaluar el modelo
y_pred = modelo.predict(X_test)
print("\nEvaluacion del modelo:")
print(classification_report(y_test, y_pred))

# 9. Guardar el modelo entrenado
joblib.dump(modelo, os.path.join("..", "modelo_entrenado.pkl"))
print("\nModelo guardado como modelo_entrenado.pkl")



