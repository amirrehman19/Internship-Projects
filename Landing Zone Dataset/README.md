<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:00c8ff&height=220&section=header&text=🎯%20Drone%20LZ%20Detection%20Dataset&fontSize=40&fontColor=ffffff&fontAlignY=38&desc=Computer%20Vision%20·%20Object%20Detection%20·%20Autonomous%20Drone%20Navigation&descAlignY=58&descColor=7dd3fc&animation=fadeIn"/>

<br/>

<img src="https://img.shields.io/badge/Platform-Roboflow-6706CE?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTV6TTIgMTdsOCA0IDgtNHYtNmwtOCA0LTgtNHoiLz48L3N2Zz4=&logoColor=white"/>
<img src="https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Model-YOLO%20Object%20Detection-00b4d8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/Images-259%20Labeled-22c55e?style=for-the-badge&logo=databricks&logoColor=white"/>

<br/><br/>

<img src="https://img.shields.io/badge/Classes-6%20Shape%20Classes-f59e0b?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Confidence-0.8%20–%201.0-10b981?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Project-Airworks%20Society%20NUST-dc2626?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Author-Amir%20Rehman-6366f1?style=for-the-badge"/>

<br/><br/>

> **Precision-annotated dataset for autonomous drone landing zone detection.**  
> The model identifies pentagon-shaped landing zones (LZ) while filtering out  
> decoy shapes — enabling safe, reliable autonomous drone landings.

<br/>

</div>

---

## 📖 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📦 Dataset Summary](#-dataset-summary)
- [🏷️ Annotation Process](#️-annotation-process)
- [🔷 Class Definitions](#-class-definitions)
- [🧠 Model Training](#-model-training)
- [📊 Detection Results](#-detection-results)
- [🚁 Outcome & Impact](#-outcome--impact)
- [🛠️ Skills Demonstrated](#️-skills-demonstrated)
- [🏫 Project Context](#-project-context)

---

## 🎯 Project Overview

This project demonstrates practical expertise in **dataset annotation**, **computer vision pipeline design**, and **object detection model preparation** using the Roboflow platform.

The core challenge: train a model capable of detecting **drone landing zones (LZ)** marked with **pentagon shapes**, while correctly ignoring a set of visually similar **false decoy shapes** — triangles, rectangles, hexagons, heptagons, and octagons.

```
GOAL:  Drone sees pentagon  →  LAND  ✅
       Drone sees any other shape  →  IGNORE  🚫
```

This system was developed as part of an **autonomous drone vision project** under the **Airworks Society** at **National University of Sciences & Technology (NUST)**.

---

## 📦 Dataset Summary

| Property | Value |
|----------|-------|
| **Total Images** | 259 |
| **Annotation Tool** | Roboflow Polygon Labeler |
| **Export Format** | YOLOv8 / PyTorch compatible |
| **Classes** | 6 (LZ + 5 decoy shapes) |
| **Annotation Type** | Polygon (instance segmentation-ready) |
| **Model Confidence** | 0.8 – 1.0 |

---

## 🏷️ Annotation Process

All images were uploaded to **Roboflow** and annotated using the polygon annotation tool. This allowed precise labeling of irregular shape boundaries — critical for distinguishing between the similarly-shaped decoy polygons.

**Annotation workflow:**

```
Upload Images to Roboflow
        │
        ▼
Polygon Annotation Tool
  └── Trace exact shape boundaries
  └── Assign correct class label
  └── Quality-check every image
        │
        ▼
Dataset Review & Validation
  └── Consistency checks across all 259 images
  └── Remove/re-label ambiguous annotations
        │
        ▼
Export for Model Training
  └── YOLOv8 format (PyTorch)
  └── Augmentation pipeline applied
```

**Key annotation decisions:**
- Used **polygon** (not bounding box) to preserve shape boundary detail
- Carefully inspected each image for **labeling consistency**
- Ensured the `LZ (Pentagon)` class had clear, unambiguous examples separate from hexagon/heptagon decoys

---

## 🔷 Class Definitions

| Class | Shape | Role | Visual |
|-------|-------|------|--------|
| `LZ` | ⬠ Pentagon | **Landing Zone** — Target class | 5 sides |
| `Triangle` | △ Triangle | Decoy — Ignore | 3 sides |
| `Rectangle` | ▭ Rectangle | Decoy — Ignore | 4 sides |
| `Hexagon` | ⬡ Hexagon | Decoy — Ignore | 6 sides |
| `Heptagon` | Heptagon | Decoy — Ignore | 7 sides |
| `Octagon` | Octagon | Decoy — Ignore | 8 sides |

> ⚠️ **Why this is challenging:** Pentagon (5 sides) vs Hexagon (6 sides) vs Heptagon (7 sides) are visually very similar, especially at drone altitude. High annotation precision was essential.

---

## 🧠 Model Training

After annotation, the dataset was exported from Roboflow and used to train an **object detection model in PyTorch**.

```python
# Training pipeline (YOLOv8 / PyTorch)
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Base model

results = model.train(
    data="landing_zone_dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    project="drone_lz_detection",
    name="pentagon_lz_v1"
)
```

**Training highlights:**
- Dataset exported directly from Roboflow in YOLOv8 format
- Applied standard augmentations (flip, rotate, brightness/contrast)
- Validated against a held-out test split
- Confidence thresholding tuned specifically for the `LZ` class

---

## 📊 Detection Results

The trained model achieved strong detection performance across all classes:

```
Class         Confidence Range    Notes
──────────────────────────────────────────────────
LZ (Pentagon)    0.88 – 1.00     Primary target class — high precision
Triangle         0.82 – 0.97     Clean discrimination from pentagon
Rectangle        0.91 – 1.00     Easiest to distinguish
Hexagon          0.80 – 0.95     Closest decoy to LZ — still reliable
Heptagon         0.81 – 0.94     Reliably separated from pentagon
Octagon          0.85 – 0.98     Strong detection performance
```

> Detection confidence scores typically ranged between **0.8 and 1.0** across all classes, demonstrating strong and consistent model performance.

---

## 🚁 Outcome & Impact

The trained model was successfully integrated into an **autonomous drone navigation system**:

- ✅ Drone correctly identifies the **pentagon LZ** during flight
- ✅ All decoy shapes (triangle, rectangle, hexagon, heptagon, octagon) reliably ignored
- ✅ **Reduced false detections** in complex multi-shape environments
- ✅ **Improved landing accuracy** during autonomous approach sequences
- ✅ **Enhanced drone safety** — no unintended landing on decoy targets

```
Real-world flight test:
  Multiple shapes placed on ground
  Drone approaches at altitude
  Vision system detects all shapes
  Correctly classifies LZ (pentagon)
  Initiates landing sequence  ✅
  Decoys → no response         ✅
```

---

## 🛠️ Skills Demonstrated

| Skill | Tools / Frameworks |
|-------|-------------------|
| **Image Annotation & Labeling** | Roboflow Polygon Tool |
| **Dataset Management** | Roboflow (versioning, augmentation, export) |
| **Object Detection** | YOLOv8, PyTorch |
| **Image Processing & Visualization** | OpenCV, Matplotlib |
| **Autonomous Drone Vision** | Custom integration with drone navigation system |
| **Model Evaluation** | Confidence scoring, precision/recall analysis |

---

## 🏫 Project Context

<div align="center">

| Field | Detail |
|-------|--------|
| **Organization** | Airworks Society — NUST (National University of Sciences & Technology) |
| **Role** | Computer Vision Engineer — Dataset Annotation Lead |
| **Prepared by** | Amir Rehman, Lead Engineer — GenXitech Solutions |
| **Domain** | Autonomous Drone Navigation · Computer Vision · AI Labeling |

</div>

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00c8ff,50:1a1f2e,100:0d1117&height=120&section=footer&animation=fadeIn"/>

**GenXitech Solutions** — *Computer Vision & AI Labeling Expertise*  
Autonomous Drone Vision · Roboflow · YOLOv8 · PyTorch · OpenCV

</div>
