import os
from flask import Blueprint, request, jsonify
import joblib
import pandas as pd

predict_bp = Blueprint('predict', __name__)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(PROJECT_ROOT, 'backend', 'models', 'price_model.pkl')
FEATURES_PATH = os.path.join(PROJECT_ROOT, 'backend', 'models', 'feature_columns.pkl')
ENCODERS_PATH = os.path.join(PROJECT_ROOT, 'backend', 'models', 'encoders.pkl')


def load_model_and_features():
    if os.path.exists(MODEL_PATH) and os.path.exists(FEATURES_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            features = joblib.load(FEATURES_PATH)
            return model, features
        except Exception:
            return None, None
    return None, None


@predict_bp.route('/', methods=['POST'])
def predict_price():
    model, feature_columns = load_model_and_features()
    if model is None or feature_columns is None:
        return jsonify({'error': 'Trained model or feature metadata not found. Run training first.'}), 503

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    try:
        input_df = pd.DataFrame([data])

        if os.path.exists(ENCODERS_PATH):
            encoders = joblib.load(ENCODERS_PATH)
            for col, encoder in encoders.items():
                if col in input_df.columns:
                    try:
                        input_df[col] = encoder.transform(input_df[col].astype(str))
                    except ValueError:
                        return jsonify({
                            'error': f"Unknown value for '{col}': '{data[col]}'. Valid options: {list(encoder.classes_)}"
                        }), 400

        input_df = input_df.reindex(columns=feature_columns, fill_value=0)
        prediction = model.predict(input_df)[0]
        return jsonify({'predicted_price': round(float(prediction), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
