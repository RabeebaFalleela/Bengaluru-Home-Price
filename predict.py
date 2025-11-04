import json, os, joblib, numpy as np

MODEL_PATH = os.path.join("models", "best_model.joblib")
COLUMNS_PATH = os.path.join("models", "columns.json")

def load_model_and_columns():
    model = joblib.load(MODEL_PATH)
    with open(COLUMNS_PATH) as f:
        cols = json.load(f)['data_columns']
    return model, cols

def predict_price(model, cols, location, sqft, bath, bhk):
    loc = (location or "other").strip().lower()
    x = np.zeros(len(cols))
    # basic assumptions
    def idx(name, default):
        try: return cols.index(name)
        except: return default
    x[idx('total_sqft',0)] = float(sqft)
    x[idx('bath',1)] = float(bath)
    x[idx('bhk',2)] = int(bhk)
    loc_col = "loc_"+loc
    if loc_col in cols:
        x[cols.index(loc_col)] = 1
    return float(model.predict([x])[0])
