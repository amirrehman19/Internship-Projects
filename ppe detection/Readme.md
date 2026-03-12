<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:ff6b00,100:ffd700&height=220&section=header&text=🦺%20PPE%20Detection%20System&fontSize=44&fontColor=ffffff&fontAlignY=38&desc=Workplace%20Safety%20·%20Computer%20Vision%20·%20YOLOv8%20Real-Time%20Detection&descAlignY=58&descColor=ffe0b2&animation=fadeIn"/>

<br/>

<img src="https://img.shields.io/badge/Model-YOLOv8-FF6B00?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Platform-Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"/>
<img src="https://img.shields.io/badge/Dataset-RoboUniverse-6706CE?style=for-the-badge&logo=databricks&logoColor=white"/>
<img src="https://img.shields.io/badge/Annotation-Roboflow-6706CE?style=for-the-badge&logoColor=white"/>

<br/><br/>

<img src="https://img.shields.io/badge/mAP%400.5-92.3%25-22c55e?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Precision-90.7%25-3b82f6?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Recall-88.5%25-a855f7?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Epochs-95%20(Early%20Stop)-ef4444?style=for-the-badge"/>

<br/><br/>

> **AI-powered Personal Protective Equipment detection for real-world workplace safety.**  
> Trained on an augmented RoboUniverse dataset with YOLOv8 — achieving **92.3% mAP@0.5**  
> and ready for edge device or server deployment.

<br/>

</div>

---

## 📖 Table of Contents

- [📜 Overview](#-overview)
- [⚡ Performance Metrics](#-performance-metrics)
- [📂 Project Workflow](#-project-workflow)
- [📦 Dataset](#-dataset)
- [🏷️ Annotation & Augmentation](#️-annotation--augmentation)
- [🧠 Model Training](#-model-training)
- [📊 Results](#-results)
- [🚀 Deployment](#-deployment)
- [🛠️ Tools & Technologies](#️-tools--technologies)

---

## 📜 Overview

This project presents a **Personal Protective Equipment (PPE) Detection System** built to enforce workplace safety compliance by automatically identifying PPE usage from images or live video feeds.

The pipeline covers the full ML lifecycle — from **dataset sourcing and annotation** through **augmentation, training, and deployment** — producing a model capable of detecting safety gear in complex, real-world industrial environments.

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

## ⚡ Performance Metrics

<div align="center">

| Metric | Score | Notes |
|:------:|:-----:|-------|
| **mAP@0.5** | **92.3%** | Mean Average Precision at IoU threshold 0.5 |
| **Precision** | **90.7%** | Low false positive rate |
| **Recall** | **88.5%** | Strong true positive detection |
| **Epochs** | **95** | Early stopping triggered |
| **Optimizer** | **AdamW** | Adaptive learning rate |

</div>

---

## 📂 Project Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. Dataset Acquisition                                     │
│     └── Sourced base dataset from RoboUniverse              │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Annotation                                              │
│     └── Labeled images in Roboflow with bounding boxes      │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Augmentation                                            │
│     └── Rotation · Brightness · Flipping · Scaling         │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Training — Google Colab (YOLOv8 + AdamW)               │
│     └── Early stopping: mAP drop for 5 consecutive epochs  │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Evaluation                                              │
│     └── mAP@0.5: 92.3%  ·  Precision: 90.7%  ·  Recall: 88.5% │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Deployment                                              │
│     └── Optimized for edge device or server integration     │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Dataset

| Property | Detail |
|----------|--------|
| **Source** | [RoboUniverse](https://universe.roboflow.com/) |
| **Annotation Tool** | Roboflow |
| **Export Format** | YOLOv8 (PyTorch) |
| **Augmentations** | Rotation, brightness, horizontal flip, scaling |

The base dataset was sourced from **RoboUniverse** and further enriched through custom annotation passes and augmentation to improve generalization in varied lighting conditions, camera angles, and industrial environments.

---

## 🏷️ Annotation & Augmentation

**Annotation** was performed using Roboflow's bounding box labeling tool. Each image was carefully reviewed to ensure consistent, accurate labels across PPE categories.

**Augmentation pipeline applied:**

```python
augmentations = {
    "rotation":      "±15°",
    "brightness":    "±25%",
    "horizontal_flip": True,
    "scaling":       "75% – 125%",
    "mosaic":        True,   # YOLOv8 default
}
```

These transformations increase dataset diversity and help the model generalize to real-world variability in lighting, perspective, and scale.

---

## 🧠 Model Training

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Pretrained base model

results = model.train(
    data     = "ppe_dataset/data.yaml",
    epochs   = 200,           # Max epochs (early stopped at 95)
    imgsz    = 640,
    batch    = 16,
    optimizer= "AdamW",
    patience = 5,             # Early stop: mAP drop for 5 epochs
    project  = "ppe_detection",
    name     = "ppe_v1"
)
```

### Training Configuration

| Parameter | Value |
|-----------|-------|
| **Model** | YOLOv8 |
| **Platform** | Google Colab |
| **Max Epochs** | 200 |
| **Final Epochs** | 95 (early stopped) |
| **Optimizer** | AdamW |
| **Loss Function** | YOLO Loss (box + cls + dfl) |
| **Input Resolution** | 640 × 640 |
| **Early Stop Condition** | `mAP@0.5` drop + `val/loss` increase for 5 epochs |

### Early Stopping Logic

```
For each epoch:
    if mAP@0.5 decreases AND val/loss increases:
        patience_counter += 1
    else:
        patience_counter = 0
        save best weights

    if patience_counter >= 5:
        STOP TRAINING  →  Load best checkpoint
```

> 📎 **[Open Google Colab Notebook](#)** ← *(replace with your actual link)*

---

## 📊 Results

### Metric Summary

```
mAP@0.5      ████████████████████░  92.3%
Precision    ████████████████████░  90.7%
Recall       ███████████████████░░  88.5%
```

### What the scores mean

- **mAP@0.5 = 92.3%** — The model correctly localizes and classifies PPE items with high overlap accuracy (IoU ≥ 0.5) across all classes.
- **Precision = 90.7%** — When the model flags a detection, it is correct 9 out of 10 times. Low false alarm rate.
- **Recall = 88.5%** — The model catches approximately 89% of all actual PPE instances in the scene, minimizing missed detections.

---

## 🚀 Deployment

The trained model is optimized and ready for integration into:

| Target | Format | Notes |
|--------|--------|-------|
| **Edge Device** (Jetson Nano, RPi) | ONNX / TFLite | Export via `model.export(format="onnx")` |
| **Server / Cloud API** | PyTorch `.pt` | Direct Ultralytics inference |
| **Web App** | ONNX + JS | Run inference in browser |
| **CCTV / IP Camera** | RTSP stream | Real-time video feed processing |

```python
# Run inference on image or video
from ultralytics import YOLO

model = YOLO("best.pt")                    # Load trained weights
results = model("worksite_image.jpg")      # Image inference
results = model("rtsp://camera_feed")      # Live CCTV stream
```

---

## 🛠️ Tools & Technologies

<div align="center">

| Category | Tool / Framework |
|----------|-----------------|
| **Annotation** | Roboflow |
| **Dataset Source** | RoboUniverse |
| **Model Architecture** | YOLOv8 (Ultralytics) |
| **Training Platform** | Google Colab |
| **Language** | Python 3.x |
| **Deep Learning** | PyTorch |
| **Object Detection** | Ultralytics YOLO |
| **Image Processing** | OpenCV, Matplotlib |
| **Export / Deploy** | ONNX, TorchScript |

</div>

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:ffd700,50:ff6b00,100:0f2027&height=120&section=footer&animation=fadeIn"/>

**PPE Detection System** — *Keeping worksites safer with AI*  
YOLOv8 · PyTorch · Roboflow · Google Colab · OpenCV

</div>
