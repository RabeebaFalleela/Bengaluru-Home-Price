Here is your **updated README.md** with a screenshot section added.
(Assuming your screenshot file is named **img1.jpg** in the project root — if not, tell me the file name.)

---

## Updated README (with screenshot)

```markdown
# Bengaluru Home Price Prediction

This project is a Streamlit-based web application that estimates residential property prices in Bengaluru.  
The model uses key features such as location, square footage, number of bedrooms (BHK), and bathrooms to generate predictions.

## Screenshots
Below is a preview of the application interface:

![App Screenshot](img1.jpg)

## Features
- Browser-based UI
- Predicts home prices across various Bengaluru locations
- Uses a trained regression model
- Lightweight and easy to run

## Methods Used
- Data cleaning and preprocessing
- Feature engineering
- One-hot encoding for categorical variables
- Linear Regression for price prediction

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

## Project Structure
```

.
├── models/
│   ├── best_model.joblib
│   └── columns.json
├── streamlit_app.py
├── predict.py
├── requirements.txt
└── README.md

```

## How to Run
1. Clone the repository:
```

git clone <repo-url>
cd Bengaluru-Home-Price

```

2. Install dependencies:
```

pip install -r requirements.txt

```

3. Launch the application:
```

streamlit run streamlit_app.py

```

## Model
The current version uses Linear Regression.  
Model and column metadata are stored under the `models/` directory.

## Future Enhancements
- Add other ML models
- Hyperparameter tuning
- Enhanced UI
- Support for additional cities

## Author
Rabeeba Falleela
```

