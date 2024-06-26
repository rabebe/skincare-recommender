from flask import Flask, render_template, request, jsonify
import pandas as pd
from preprocessing import merge_data
from hybrid import hybrid_recommendation_system

app = Flask(__name__)

# File paths for data
file1_path = "data/product_info.csv"
file2_path = "data/reviews_0-250.csv"
on_column = "product_id"

# Preprocess data once at the start
preprocessed_df = merge_data(file1_path, file2_path, on_column)
preprocessed_df = preprocessed_df.sample(10000, random_state=42)

@app.route('/')
def index():
    """
    Render the main index page.
    """
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Handle the recommendation request.
    Expects a JSON payload with 'skin_type'.
    Returns a JSON response with product recommendations.
    """
    data = request.get_json()
    user_skin_type = data.get('skin_type')

    # Get recommendations based on user skin type
    recommendations = hybrid_recommendation_system(preprocessed_df, user_skin_type)

    # Format the recommendations as a JSON response
    return jsonify(recommendations=[{"name": rec, "url": "#"} for rec in recommendations])

if __name__ == '__main__':
    app.run(debug=True)