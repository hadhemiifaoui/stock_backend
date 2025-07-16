
import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'ml_models')

model = joblib.load(os.path.join(MODEL_DIR, 'model_fmp.pkl'))
label_encoder = joblib.load(os.path.join(MODEL_DIR, 'label_encoder.pkl'))
model_columns = joblib.load(os.path.join(MODEL_DIR, 'model_columns.pkl'))

def predict_fmp(input_data):
    df = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df_encoded)
    return label_encoder.inverse_transform(prediction)[0]
