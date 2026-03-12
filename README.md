# 💼 Internship Projects Portfolio
### Electronics · IoT · Computer Vision · Machine Learning

> 🚀 *A collection of internship projects spanning embedded IoT systems, AI-powered computer vision, machine learning, and analog circuit design.*

[![GitHub](https://img.shields.io/badge/GitHub-amirrehman19-black?style=flat-square&logo=github)](https://github.com/amirrehman19)
[![Organization](https://img.shields.io/badge/Organization-GenXI%20Tech%20Solutions-orange?style=flat-square)](https://www.genxitechsolutions.com/)
[![University](https://img.shields.io/badge/University-NUST%20PNEC-darkblue?style=flat-square)](https://www.nust.edu.pk)
[![Status](https://img.shields.io/badge/All%20Projects-Completed-success?style=flat-square)]()

---

## 📁 Projects Index

| # | Project | Domain | Tools |
|---|---------|--------|-------|
| 1 | [🚦 Smart Web-Controlled Traffic Light System](#-project-1--smart-web-controlled-traffic-light-system) | IoT / Embedded / Networking | ESP32 · Arduino · ENC28J60 |
| 2 | [🎯 Drone Landing Zone Detection Dataset](#-project-2--drone-landing-zone-detection-dataset) | Computer Vision / AI | Roboflow · YOLOv8 · PyTorch |
| 3 | [🦺 PPE Detection System](#-project-3--ppe-detection-system) | Computer Vision / AI | YOLOv8 · Google Colab · Roboflow |
| 4 | [⚡ Auto Cut-Off Charger for Scooty](#-project-4--auto-cut-off-charger-for-scooty) | Analog Electronics / Circuit Design | Proteus · LM358 · Relay |
| 5 | [📱 Spam SMS Detection](#-project-5--spam-sms-detection) | Machine Learning / NLP | Python · scikit-learn · TF-IDF |

---
---

## 🚦 Project 1 — Smart Web-Controlled Traffic Light System

[![Domain](https://img.shields.io/badge/Domain-IoT%20%2F%20Embedded-blue?style=flat-square)]()
[![MCU](https://img.shields.io/badge/MCU-ESP32%20%2B%20Arduino%20Nano-red?style=flat-square)]()
[![Network](https://img.shields.io/badge/Network-ENC28J60%20Ethernet-green?style=flat-square)]()
[![LEDs](https://img.shields.io/badge/LEDs-354%20per%20array-yellow?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)]()

### 📌 Overview

A **smart, web-controlled traffic light system** for highways and toll booths. Red and green high-power LED arrays signal **Stop & Pay** or **Payment Complete**, controlled remotely over a network using **ESP32**, **ENC28J60**, and **Arduino Nano**.

---

### 🏗️ System Architecture

```
OPERATOR TERMINAL
Browser → http://<ip>/stop  or  /go
                │
                ▼ HTTP GET (LAN)
┌──────────────────────────────┐
│   ENC28J60 Ethernet Module   │◄── SPI ──► ESP32
└──────────────────────────────┘
                │
                ▼
┌──────────────────────────────┐
│         ESP32 Core           │
│  Parses URL → Sets GPIO      │
└──────────────────────────────┘
                │
                ▼
┌──────────────────────────────┐
│       Arduino Nano           │
│    (Relay Drive Logic)       │
└──────────────────────────────┘
                │
                ▼
┌───────────────────────────────────┐
│     8-Channel Relay Module        │
│  LN1–LN4 (RED) │ LN5–LN8 (GREEN) │
└───────┬─────────────────┬─────────┘
        ▼                 ▼
  🔴 RED ARRAY      🟢 GREEN ARRAY
   (354 LEDs)        (354 LEDs)
  [ STOP / PAY ]   [ GO / CLEAR ]
```

---

### ⚙️ Hardware Components

| # | Component | Spec | Role |
|---|-----------|------|------|
| 1 | `ESP32 Dev Board` | WROOM-32 | HTTP web server + controller |
| 2 | `ENC28J60` | SPI, 3.3V | Wired network interface |
| 3 | `Arduino Nano` | ATmega328P | Relay control logic |
| 4 | `8-Channel Relay` | 5V, 10A/250VAC | Power switching |
| 5 | `LED Array — Red` | 354 LEDs | STOP signal |
| 6 | `LED Array — Green` | 354 LEDs | GO signal |
| 7 | `LED Driver Board` | Constant current × 2 | Drive LED arrays |
| 8 | `Weatherproof Enclosure` | IP65+ | Outdoor mounting |

---

### 🌐 Web API Endpoints

| Endpoint | Action | Result |
|----------|--------|--------|
| `GET /stop` | 🔴 RED ON / 🟢 GREEN OFF | Stop & Pay signal |
| `GET /go` | 🟢 GREEN ON / 🔴 RED OFF | Payment Complete |
| `GET /status` | — | Returns JSON state |

```bash
curl http://192.168.1.50/stop    # Activate STOP
curl http://192.168.1.50/go      # Activate GO
curl http://192.168.1.50/status  # {"state":"go","red":false,"green":true}
```

---

### 🛠️ Tools & Technologies
`ESP32` · `ENC28J60` · `Arduino Nano` · `8-Channel Relay` · `REST API` · `IoT` · `HTTP Server` · `SPI`

---
---

## 🎯 Project 2 — Drone Landing Zone Detection Dataset

[![Domain](https://img.shields.io/badge/Domain-Computer%20Vision%20%2F%20AI-blueviolet?style=flat-square)]()
[![Platform](https://img.shields.io/badge/Platform-Roboflow-6706CE?style=flat-square)]()
[![Model](https://img.shields.io/badge/Model-YOLOv8-00b4d8?style=flat-square)]()
[![Images](https://img.shields.io/badge/Images-259%20Labeled-22c55e?style=flat-square)]()
[![Classes](https://img.shields.io/badge/Classes-6%20Shape%20Classes-f59e0b?style=flat-square)]()
[![Confidence](https://img.shields.io/badge/Confidence-0.8%20–%201.0-success?style=flat-square)]()

### 📌 Overview

A **precision-annotated dataset** for autonomous drone landing zone detection. The model identifies **pentagon-shaped landing zones (LZ)** while filtering out decoy shapes — enabling safe, reliable autonomous drone landings.

> Developed under the **Airworks Society** at **NUST** in collaboration with **GenXI Tech Solutions**.

```
GOAL:  Drone sees pentagon  →  LAND  ✅
       Drone sees any other shape  →  IGNORE  🚫
```

---

### 📦 Dataset Summary

| Property | Value |
|----------|-------|
| 🖼️ Total Images | **259** |
| 🏷️ Annotation Tool | Roboflow Polygon Labeler |
| 📤 Export Format | YOLOv8 / PyTorch |
| 🔢 Classes | **6** (LZ + 5 decoy shapes) |
| 📐 Annotation Type | Polygon (instance segmentation-ready) |
| 🎯 Confidence Range | **0.8 – 1.0** |

---

### 🔷 Class Definitions

| Class | Shape | Role |
|-------|-------|------|
| `LZ` | ⬠ Pentagon | ✅ **Landing Zone — Target** |
| `Triangle` | △ Triangle | 🚫 Decoy — Ignore |
| `Rectangle` | ▭ Rectangle | 🚫 Decoy — Ignore |
| `Hexagon` | ⬡ Hexagon | 🚫 Decoy — Ignore |
| `Heptagon` | Heptagon | 🚫 Decoy — Ignore |
| `Octagon` | Octagon | 🚫 Decoy — Ignore |

> ⚠️ Pentagon vs Hexagon vs Heptagon are visually very similar at altitude — high annotation precision was essential.

---

### 📊 Detection Results

| Class | Confidence Range | Notes |
|-------|-----------------|-------|
| `LZ (Pentagon)` | 0.88 – 1.00 | Primary target — high precision |
| `Triangle` | 0.82 – 0.97 | Clean discrimination |
| `Rectangle` | 0.91 – 1.00 | Easiest to distinguish |
| `Hexagon` | 0.80 – 0.95 | Closest decoy to LZ |
| `Heptagon` | 0.81 – 0.94 | Reliably separated |
| `Octagon` | 0.85 – 0.98 | Strong performance |

---

### 🛠️ Tools & Technologies
`Roboflow` · `YOLOv8` · `PyTorch` · `OpenCV` · `Polygon Annotation` · `Autonomous Drone Vision`

---
---

## 🦺 Project 3 — PPE Detection System

[![Domain](https://img.shields.io/badge/Domain-Computer%20Vision%20%2F%20Safety%20AI-orange?style=flat-square)]()
[![Model](https://img.shields.io/badge/Model-YOLOv8-FF6B00?style=flat-square)]()
[![Platform](https://img.shields.io/badge/Platform-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab)]()
[![mAP](https://img.shields.io/badge/mAP%400.5-92.3%25-22c55e?style=flat-square)]()
[![Precision](https://img.shields.io/badge/Precision-90.7%25-3b82f6?style=flat-square)]()
[![Recall](https://img.shields.io/badge/Recall-88.5%25-a855f7?style=flat-square)]()

### 📌 Overview

An **AI-powered PPE (Personal Protective Equipment) Detection System** for real-world workplace safety compliance. Trained on an augmented RoboUniverse dataset with YOLOv8 — achieving **92.3% mAP@0.5**.

```
Camera / Video Feed
       │
       ▼
  YOLOv8 Inference
       │
  ┌────┴─────┐
  ▼          ▼
✅ PPE       ❌ No PPE
Compliant    Alert Triggered
```

---

### ⚡ Performance Metrics

| Metric | Score | Meaning |
|--------|-------|---------|
| 🎯 **mAP@0.5** | **92.3%** | Correct localization + classification at IoU ≥ 0.5 |
| 🔵 **Precision** | **90.7%** | 9/10 detections are correct — low false alarms |
| 🟣 **Recall** | **88.5%** | Catches ~89% of all PPE instances |
| ⏱️ **Epochs** | **95** | Early stopping triggered |
| ⚙️ **Optimizer** | **AdamW** | Adaptive learning rate |

---

### 🧠 Training Configuration

| Parameter | Value |
|-----------|-------|
| Model | YOLOv8 |
| Platform | Google Colab |
| Max Epochs | 200 (stopped at 95) |
| Optimizer | AdamW |
| Input Resolution | 640 × 640 |
| Early Stop | mAP drop + val/loss rise for 5 epochs |

---

### 🚀 Deployment Targets

| Target | Format |
|--------|--------|
| Edge Device (Jetson/RPi) | ONNX / TFLite |
| Server / Cloud API | PyTorch `.pt` |
| Web App | ONNX + JS |
| CCTV / IP Camera | RTSP stream |

---

### 🛠️ Tools & Technologies
`YOLOv8` · `PyTorch` · `Roboflow` · `Google Colab` · `OpenCV` · `RoboUniverse` · `ONNX`

---
---

## ⚡ Project 4 — Auto Cut-Off Charger for Scooty

[![Domain](https://img.shields.io/badge/Domain-Analog%20Electronics-yellow?style=flat-square)]()
[![IC](https://img.shields.io/badge/IC-LM358%20Comparator-orange?style=flat-square)]()
[![Voltage](https://img.shields.io/badge/Battery-12V%20Lead--Acid-red?style=flat-square)]()
[![Simulation](https://img.shields.io/badge/Simulation-Proteus-blueviolet?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)]()

### 📌 Overview

A **safe and reliable automatic charging circuit** for a 12V scooter battery — designed to prevent overcharging and extend battery life using relay switching, voltage sensing, and an LM358 comparator.

```
AC Mains → Transformer → Bridge Rectifier → Filter Caps
                                    │
                                    ▼
                          LM358 Comparator
                          (Monitors battery voltage)
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
            Voltage < Threshold             Voltage = Full
            🟢 Green LED ON                 🔴 Red LED ON
            Relay CLOSED                   Relay OPEN
            Charging IN PROGRESS           Charging CUT OFF
```

---

### 🔧 Working Principle

The comparator continuously monitors battery voltage against a **preset reference** (set via potentiometer RV1). When the battery reaches full charge voltage, the comparator triggers the relay to **disconnect the charger** — protecting the battery from overcharging.

---

### 🧩 Component List

| Component | Description | Qty |
|-----------|-------------|-----|
| `TR1` | 230V AC to 12V AC Transformer | 1 |
| `BR1` | Bridge Rectifier | 1 |
| `C1` | Electrolytic Capacitor 1000µF/25V | 1 |
| `C2` | Electrolytic Capacitor 100µF/25V | 1 |
| `U1` | LM358 Comparator IC | 1 |
| `R1` | Resistor 10 kΩ | 1 |
| `R2` | Resistor 220 Ω | 1 |
| `R4` | Resistor 1 kΩ | 1 |
| `R5` | Resistor 1 Ω | 1 |
| `R6` | Resistor 1 MΩ | 1 |
| `RV1` | Preset Potentiometer 15 kΩ | 1 |
| `Q1` | BC547 NPN Transistor | 1 |
| `RL1` | 12V Relay | 1 |
| `D1,D3,D9,D10` | 1N4007 Diodes | 4 |
| `D2` | 6A10 Diode | 1 |
| `D5` | LED Green (Charging) | 1 |
| `D7, D8` | LED Red (Cut-Off) | 2 |
| `D11` | 1N4738A Zener Diode | 1 |

---

### 💡 LED Indicators

| LED | Color | Status |
|-----|-------|--------|
| D5 | 🟢 Green | Charging in progress |
| D7, D8 | 🔴 Red | Battery full — charging cut off |

---

### ✅ Key Features

- ✅ **Automatic Cut-Off** — stops charging at full voltage
- ✅ **Overcharge Protection** — extends battery lifespan
- ✅ **Relay-Based Switching** — safe current handling
- ✅ **LM358 Comparator** — precision voltage sensing
- ✅ **DIY-Friendly** — readily available components

---

### 🛠️ Tools & Technologies
`LM358 Comparator` · `Relay Switching` · `Proteus Simulation` · `Analog Circuit Design` · `12V Battery Charging` · `BC547 Transistor`

---
---

## 📱 Project 5 — Spam SMS Detection

[![Domain](https://img.shields.io/badge/Domain-Machine%20Learning%20%2F%20NLP-blue?style=flat-square)]()
[![Model](https://img.shields.io/badge/Models-Naive%20Bayes%20%2B%20Logistic%20Regression-green?style=flat-square)]()
[![Accuracy](https://img.shields.io/badge/Accuracy-97–99%25-success?style=flat-square)]()
[![Dataset](https://img.shields.io/badge/Dataset-SMS%20Spam%20Collection-orange?style=flat-square)]()
[![Platform](https://img.shields.io/badge/Platform-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab)]()

### 📌 Overview

A **binary text classifier** that detects spam SMS messages using **NLP** and two ML models — **Naive Bayes** and **Logistic Regression** — with TF-IDF vectorization.

```
Enter SMS: "Congratulations! You've won a free prize. Click here!"
                    │
                    ▼
           TF-IDF Vectorization
           (top 5,000 features)
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
    Naive Bayes        Logistic Regression
          │                    │
          └─────────┬──────────┘
                    ▼
           🧠 Prediction: 📩 SPAM
```

---

### 📊 Dataset

| Property | Value |
|----------|-------|
| 📦 Dataset | SMS Spam Collection |
| 📝 Total Messages | **5,572** |
| ✅ Ham (Legitimate) | ~4,825 |
| 🚫 Spam | ~747 |
| 🔗 Source | UCI ML Repository / Kaggle |

---

### 📈 Model Results

| Model | Accuracy | Notes |
|-------|----------|-------|
| 🧠 **Naive Bayes** | ~97–98% | Fast, probabilistic — ideal for text |
| 📈 **Logistic Regression** | ~98–99% | Linear model, strong generalization |

Both evaluated with:
- ✅ Accuracy Score
- ✅ Precision / Recall / F1-Score (classification report)

---

### ⚙️ Pipeline

```
Load spam.csv
      │
      ▼
Preprocess Text
      │
      ▼
TF-IDF Vectorization (5,000 features)
      │
      ▼
80/20 Train-Test Split
      │
   ┌──┴──┐
   ▼     ▼
  NB    LR
   └──┬──┘
      ▼
Evaluate → Accuracy + Classification Report
      │
      ▼
Interactive Prediction (user input)
```

---

### 🖥️ Quick Start

```bash
# Install dependencies
pip install pandas scikit-learn

# Run the classifier
python spam_sms_detection.py

# Enter a message to classify:
# → "Win a FREE iPhone now! Click here"
# → 🧠 Prediction: 📩 SPAM
```

---

### 📁 Project Structure

```
spam-sms-detection/
├── spam_sms_detection.py   ← Main script
├── spam.csv                ← Dataset
└── README.md               ← Documentation
```

---

### 🛠️ Tools & Technologies
`Python` · `scikit-learn` · `TF-IDF` · `Naive Bayes` · `Logistic Regression` · `pandas` · `Google Colab` · `NLP`

---
---

## 👤 About

| | |
|-|---|
| 👨‍💻 **Intern** | Amir Rehman |
| 🏛️ **Institution** | NUST — PNEC, Karachi |
| 🤝 **Organization** | GenXI Tech Solutions |
| 🌐 **GitHub** | [@amirrehman19](https://github.com/amirrehman19) |
| 💼 **Upwork** | [amirrehman]([https://www.upwork.com](https://www.upwork.com/freelancers/~011ffb2a25924b0049?s=1031626803146899456)) |
| 📅 **Year** | 2026 |

---

> *These internship projects span IoT hardware, AI/ML, computer vision, and analog circuit design — reflecting hands-on engineering experience across a broad range of real-world domains.*
