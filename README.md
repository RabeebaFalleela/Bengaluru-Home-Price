```markdown
# 🏘️ Bengaluru Home Price Predictor

A lightweight web application that estimates residential property prices across Bengaluru.  
Just provide location, square footage, BHK, and bathroom count — the app returns an approximate market value.

---

## 📸 Screenshots

| App Preview |
|-------------|
| ![App Screenshot](img1.jpg) |

---

## 🚀 What This App Does

- Predicts house prices based on:
  - Location
  - Total square footage
  - BHK count
  - Number of bathrooms
- Simple UI built using Streamlit
- Fast inference using a pre-trained ML model

---

## 🧠 How It Works

The project uses:
- Data preprocessing + cleaning
- Feature engineering
- One-hot encoding for categorical variables
- Regression-based ML model (trained on Bengaluru housing data)

Trained artifacts are stored under `models/`.

---

## 🧰 Tech Stack

- Python
- Scikit-learn
- Pandas / NumPy
- Streamlit
- Joblib

---

## 📁 Folder Overview

```

.
├── models/
│   ├── best_model.joblib
│   └── columns.json
├── predict.py
├── streamlit_app.py
├── requirements.txt
├── img1.jpg
└── README.md

```

---

## ▶️ Run the App Locally

1) Clone repository  
```

git clone <your-repo-url>
cd Bengaluru-Home-Price

```

2) Install dependencies  
```

pip install -r requirements.txt

```

3) Launch Streamlit  
```

streamlit run streamlit_app.py

```

---

## 📦 Model

The current version uses Linear Regression.
You can later try:
- Random Forest
- XGBoost
- Hyperparameter tuning

---

## ✅ Future Improvements

- Add more model options
- Improve UI
- Include more property parameters
- Deploy publicly

---

## ✨ Author

**Rabeeba Falleela**

```


