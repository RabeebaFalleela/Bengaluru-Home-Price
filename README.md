# Streamlit Bengaluru Home Price Predictor

---

##  1) Setup

```bash
pip install -r requirements.txt
````

---

##  2) Place Model Files

Place the following files inside the `models/` directory:

```
models/
 ── best_model.joblib
 ── columns.json
```

---

##  3) Run the App

```bash
streamlit run streamlit_app.py
```

---

##  Project Structure

```
.
── models/
  ── best_model.joblib
  ── columns.json
── streamlit_app.py
── requirements.txt
── README.md
```

---

##  Features

* Predicts Bengaluru house prices
* Clean Streamlit UI
* Accepts details like:

  * Location
  * BHK
  * Bathrooms
  * Total Sqft

---

##  Requirements

```
Python 3.9+
Streamlit
Scikit-learn
Pandas
NumPy
```

---

##  Example Prediction Flow

1. Select Bengaluru location
2. Choose BHK count
3. Enter bathroom count
4. Enter total square-foot area
5. Get predicted price instantly 🎯

---

##  Notes

* Ensure model + columns file are present inside `models/`
* Values outside training range may reduce accuracy

---

##  Future Enhancements

* Add visualization
* Allow CSV batch prediction
* Cloud deployment

---


---


