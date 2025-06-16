# 🚦 NetCongestionPredictorAI

**NetCongestionPredictorAI** es un proyecto simple de aprendizaje automático para predecir congestión en redes usando estadísticas de tráfico y un modelo supervisado de clasificación.

---

## 🚀 Descripción del Proyecto

Este proyecto entrena un modelo de **machine learning** que detecta cuándo una red está **congestionada**, en base a características como:

- Uso de ancho de banda
- Tasa de paquetes
- Latencia
- Jitter (variación en latencia)

También cuenta con una API implementada en **FastAPI**, que permite hacer predicciones en tiempo real mediante peticiones HTTP.

---

## 📊 Dataset

El conjunto de datos fue creado manualmente, a partir de capturas de tráfico con Wireshark. Cada fila representa una muestra del estado de la red en un momento dado.

### 🧾 Columnas del dataset:
- `tiempo` — timestamp
- `ancho_banda_usado` — ancho de banda (kbps)
- `paquetes_usados` — total de paquetes
- `paquetes_por_segundo` — tasa de paquetes
- `latencia` — latencia (ms)
- `jitter` — jitter (ms)
- `congestion` — etiqueta binaria (1: congestión, 0: normal)

> La columna `congestion` se determinó por reglas: se marca como 1 si **2 o más** de estas condiciones se cumplen:
- ancho_banda_usado > 700  
- paquetes_por_segundo > 800  
- latencia > 200 ms  
- jitter > 80 ms

---

## 🧠 Modelo

Se utilizó un **Random Forest Classifier** (`scikit-learn`):

- Entrenado con el 80% del dataset
- Evaluado con el 20% restante
- Buen rendimiento (precisión y recall equilibrados)
- Guardado como archivo `modelo_entrenado.pkl` para uso posterior

---

## ⚙️ API REST (FastAPI)

Se implementó una **API en FastAPI** para realizar predicciones en tiempo real.

### 🚀 Cómo ejecutar la API

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
