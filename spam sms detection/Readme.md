
# 📱 Spam SMS Detection

A machine learning project that classifies SMS messages as **spam** or **ham (legitimate)** using Natural Language Processing (NLP) techniques and two classification models: Naive Bayes and Logistic Regression.

---

## 🚀 Demo

```
Enter an SMS Email Message to classify: Congratulations! You've won a free prize. Click here to claim now!

🧠 Prediction: 📩 SPAM
```

---

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Models & Results](#models--results)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)

---

## Overview

This project builds a binary text classifier to detect spam SMS messages. It uses **TF-IDF vectorization** to convert raw text into numerical features, then trains two machine learning models for comparison.

Key steps:
1. Load and preprocess the SMS Spam Collection dataset
2. Vectorize text with TF-IDF (top 5,000 features)
3. Train Naive Bayes and Logistic Regression classifiers
4. Evaluate both models with accuracy and classification reports
5. Interactively classify new messages via user input

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, a well-known public dataset containing 5,572 labeled SMS messages.

| Label | Count | Description |
|-------|-------|-------------|
| ham   | ~4,825 | Legitimate messages |
| spam  | ~747   | Spam messages |

**Download:** [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) or [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

Save the file as `spam.csv` in your working directory.

---

## ⚙️ Installation

### Prerequisites

- Python 3.7+
- pip

### Install Dependencies

```bash
pip install pandas scikit-learn
```

If running on **Google Colab**, all dependencies are pre-installed.

---

## 🖥️ Usage

### Google Colab

1. Open the notebook in [Google Colab](https://colab.research.google.com/)
2. Upload `spam.csv` when prompted
3. Run all cells in order
4. Enter a message when prompted to classify it

### Local Environment

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/spam-sms-detection.git
   cd spam-sms-detection
   ```

2. Place `spam.csv` in the project directory

3. Run the script:
   ```bash
   python spam_sms_detection.py
   ```

4. Enter a message to classify when prompted

---

## 📈 Models & Results

Both models are trained on an 80/20 train-test split.

### Naive Bayes (MultinomialNB)
- Fast, probabilistic model well-suited for text classification
- Typically achieves **~97–98% accuracy** on this dataset

### Logistic Regression
- Linear model with strong generalization
- Typically achieves **~98–99% accuracy** on this dataset

Both models are evaluated using:
- **Accuracy Score**
- **Precision, Recall, F1-Score** (via classification report)

> Results may vary slightly due to random state in train/test split.

---

## 📁 Project Structure

```
spam-sms-detection/
│
├── spam_sms_detection.py   # Main script
├── spam.csv                # Dataset (download separately)
└── README.md               # Project documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| pandas | Data loading & manipulation |
| scikit-learn | ML models, TF-IDF, evaluation |
| Google Colab | Cloud notebook environment |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements such as:
- Adding more models (SVM, Random Forest, etc.)
- Improving text preprocessing (stemming, lemmatization)
- Building a web interface with Flask or Streamlit

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
