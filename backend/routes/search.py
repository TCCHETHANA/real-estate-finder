import os
from flask import Blueprint, request, jsonify
import pandas as pd

search_bp = Blueprint('search', __name__)

# Attempt to locate processed data; load if available, otherwise keep None
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_PATH = os.path.join(PROJECT_ROOT, 'ml', 'data', 'processed', 'properties_cleaned.csv')

df = None
if os.path.exists(DATA_PATH):
    try:
        df = pd.read_csv(DATA_PATH)
    except Exception:
        df = None


@search_bp.route('/', methods=['GET'])
def search_properties():
    """Search properties using optional filters.

    Query params supported: budget_min, budget_max, location, amenities
    """
    if df is None:
        return jsonify({'error': 'Processed dataset not found. Run preprocessing first.'}), 503

    # Read query parameters
    try:
        budget_min = float(request.args.get('budget_min', 0))
        budget_max = float(request.args.get('budget_max', 1e12))
    except ValueError:
        return jsonify({'error': 'Invalid budget values'}), 400

    location = request.args.get('location')
    amenities = request.args.get('amenities')

    results = df.copy()
    results = results[(results['price'] >= budget_min) & (results['price'] <= budget_max)]

    if location and 'location' in results.columns:
        results = results[results['location'].str.contains(location, case=False, na=False)]

    if amenities and 'amenities' in results.columns:
        amenity_list = [a.strip().lower() for a in amenities.split(',')]
        results = results[results['amenities'].apply(lambda x: all(a in str(x).lower() for a in amenity_list))]

    return jsonify(results.head(20).to_dict(orient='records'))
