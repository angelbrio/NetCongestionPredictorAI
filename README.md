# 🚦 NetCongestionPredictorAI

**NetCongestionPredictorAI** is a simple machine learning project that predicts network congestion using traffic statistics and a supervised classification model.

---

## 🚀 Project Overview

This project trains a **machine learning model** to detect when a network is **congested**, based on features such as:

- Bandwidth usage
- Packet rate
- Latency
- Jitter

It also includes a **FastAPI**-powered REST API that allows for real-time congestion predictions via HTTP requests.

---

## 📊 Dataset

The dataset was manually crafted from Wireshark captures. Each row represents a snapshot of network conditions at a given time.

### 🧾 Dataset Columns:

- `tiempo` — timestamp
- `ancho_banda_usado` — bandwidth used (kbps)
- `paquetes_usados` — total packets
- `paquetes_por_segundo` — packets per second
- `latencia` — latency (ms)
- `jitter` — jitter (ms)
- `congestion` — binary label (1 = congested, 0 = normal)

> The `congestion` label is set to 1 (congested) if **two or more** of the following are true:
- bandwidth used > 700  
- packets per second > 800  
- latency > 200 ms  
- jitter > 80 ms

---

## 🧠 Model

A **Random Forest Classifier** (`scikit-learn`) is used for training:

- Trained on 80% of the dataset
- Evaluated on the remaining 20%
- Delivers balanced precision and recall
- Saved as `modelo_entrenado.pkl` for reuse

---

## ⚙️ REST API (FastAPI)

The project includes a **FastAPI** service for real-time predictions.

### 🚀 How to Run the API

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

