# NetCongestionPredictorAI

# NetCongestionPredictorAI

A simple machine learning project to predict **network congestion** using supervised learning and traffic statistics.

## 🚀 Project Overview

This project trains a machine learning model to detect when a network is congested based on several features such as bandwidth usage, packet rates, latency, and jitter.

The main goal is to demonstrate the application of AI in network systems — as a small, practical proof of concept.

---

## 📊 Dataset

The dataset was manually created as a small sample using network traffic statistics captured from **Wireshark**.

Each row simulates a snapshot of network conditions, with the following features:

- `tiempo` (time)
- `ancho_banda_usado` (bandwidth used)
- `paquetes_usados` (total packets)
- `paquetes_por_segundo` (packets per second)
- `latencia` (latency in ms)
- `jitter` (variation in latency in ms)
- `congestion` (1 if network is congested, 0 otherwise)

The label `congestion` was manually derived based on a rule-based system. A record is marked as congested (`1`) if **two or more** of the following are true:

- Bandwidth used > 700
- Packets per second > 800
- Latency > 200 ms
- Jitter > 80 ms

---

## 🧠 Model

The model used is a **Random Forest Classifier**, implemented using [`scikit-learn`](https://scikit-learn.org/):

- It was trained on a subset of the data (80%)
- The remaining 20% was used for evaluation
- The model achieved good accuracy and balanced precision/recall
- The trained model is saved as a `.pkl` file for later inference

---

## 📂 Project Structure

