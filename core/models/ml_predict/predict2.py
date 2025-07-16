import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'ml_models')

# Load model and column names
model = joblib.load(os.path.join(MODEL_DIR, 'regression_model.pkl'))
model_columns = joblib.load(os.path.join(MODEL_DIR, 'model_columns1.pkl'))

def predict_score(input_data: dict):
    df = pd.DataFrame([input_data])

    df_encoded = pd.get_dummies(df)

    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[model_columns]

    prediction = model.predict(df_encoded)

    return {
        "SCORE": float(prediction[0])
    }
