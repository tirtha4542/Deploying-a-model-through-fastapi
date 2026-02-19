
# 🩺 Diabetes Prediction API

A production-ready REST API built with **FastAPI** that predicts the likelihood of diabetes in patients based on medical diagnostic measurements. The project utilizes a **Support Vector Machine (SVM)** model and implements data normalization to ensure high prediction accuracy.

## 🚀 Project Overview

This project provides an end-to-end machine learning pipeline:

1. **Data Processing:** Normalization of raw medical data using `StandardScaler`.
2. **Model Training:** A Classification model trained on the PIMA Diabetes Dataset.
3. **API Deployment:** A FastAPI server that accepts JSON inputs and returns real-time predictions.

## 🛠️ Tech Stack

* **Language:** Python 3.13
* **Machine Learning:** Scikit-learn, NumPy, Pandas
* **API Framework:** FastAPI, Uvicorn, Pydantic
* **Serialization:** Pickle

---

## 📂 Project Structure

```text
capstone_project_1/
├── ml_api.py             # FastAPI server script
├── diabetic_model.sav    # Trained SVM model (Pickle file)
├── scaler.sav            # Trained StandardScaler (Pickle file)
├── requirements.txt      # Project dependencies
└── test_api.py           # Client script to test the API

```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/diabetes-prediction-api.git
cd diabetes-prediction-api

```


2. **Create a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install fastapi uvicorn scikit-learn pandas requests

```


4. **Run the API:**
```bash
uvicorn ml_api:app --reload

```


The API will be live at: `http://127.0.0.1:8000`

---

## 🧪 Usage

### API Endpoint: `POST /diabetics_prediction`

The API expects a JSON object containing the following patient metrics:

| Field | Type | Description |
| --- | --- | --- |
| `Pregnancies` | int | Number of times pregnant |
| `Glucose` | int | Plasma glucose concentration |
| `BloodPressure` | int | Diastolic blood pressure (mm Hg) |
| `SkinThickness` | int | Triceps skin fold thickness (mm) |
| `Insulin` | int | 2-Hour serum insulin (mu U/ml) |
| `BMI` | float | Body mass index (weight in kg/(height in m)^2) |
| `DiabetesPedigreeFunction` | float | Diabetes pedigree function |
| `Age` | int | Age (years) |

### Example Request (Python)

```python
import requests

data = {
    "Pregnancies": 1,
    "Glucose": 126,
    "BloodPressure": 60,
    "SkinThickness": 0,
    "Insulin": 0,
    "BMI": 30.1,
    "DiabetesPedigreeFunction": 0.349,
    "Age": 47
}

response = requests.post("http://127.0.0.1:8000/diabetics_prediction", json=data)
print(response.text) # Returns: "The person is diabetic"

```

---

## 🔑 Key Learnings

* **Feature Scaling:** Learned the importance of persisting the `StandardScaler` alongside the model to prevent "data drift" during inference.
* **Data Validation:** Implemented **Pydantic** models to ensure the API only processes valid data types.
* **REST Architecture:** Developed a clean POST endpoint for model interaction.

