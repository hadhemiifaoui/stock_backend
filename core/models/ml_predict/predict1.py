# import os
# import joblib
# import pandas as pd
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_DIR = os.path.join(BASE_DIR, '..', 'ml_models')
#
# model = joblib.load(os.path.join(MODEL_DIR, 'multi_output_model.pkl'))
#
# model_columns = joblib.load(os.path.join(MODEL_DIR, 'model_columns.pkl'))
#
#
# def predict_score_and_fmp(input_data):
#     df = pd.DataFrame([input_data])
#
#     df_encoded = pd.get_dummies(df)
#
#     df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)
#
#     prediction = model.predict(df_encoded)
#
#     score = prediction[0][0]
#     frequance_mp = prediction[0][1]
#
#
#
#     return {
#         'score': score,
#         'frequance_mp': frequance_mp,
#     }


import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'ml_models')

model = joblib.load(os.path.join(MODEL_DIR, 'multi_output_model.pkl'))
model_columns = joblib.load(os.path.join(MODEL_DIR, 'model_columns.pkl'))

def predict_score_and_fmp(input_data: dict):

    df = pd.DataFrame([input_data])

    df_encoded = pd.get_dummies(df)


    missing_cols = [col for col in model_columns if col not in df_encoded.columns]
    for col in missing_cols:
        df_encoded[col] = 0
    df_encoded = df_encoded[model_columns]


    prediction = model.predict(df_encoded)
    return {
        "SCORE": prediction[0][0],
        "Fréquance_MP": prediction[0][1]
    }
