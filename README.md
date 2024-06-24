# Skincare Recommender

## Overview
* The Skincare Recommender System is a project designed to provide personalized skincare product recommendations based on a user's skin type.
* This system combines various recommendation techniques, including content-based filtering, collaborative filtering, and sentiment analysis, to suggest the most suitable products for users.

## Features
Content-Based Filtering: Recommends products based on the textual features and highlights of other products.
Collaborative Filtering: Uses user reviews and ratings to recommend products liked by similar users.
Sentiment Analysis: Analyzes user reviews to filter and recommend products based on sentiment.

## Prerequisites
Python 3.7 or higher
Flask
Pandas
Scikit-learn
NLTK (Natural Language Toolkit)

## Installation

```bash
git clone https://github.com/yourusername/skincare-recommender.git
cd skincare-recommender
```
Install the required repositories
```bash
pip install -r requirements.txt
```

## Data Preparation
Ensure you have the necessary data files in the '/data' folder:
* product_info.csv: Contains information about skincare products.
reviews_0-250.csv: Contains reviews and ratings of the products.
The dataset was obtained from Kaggle: https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews?select=product_info.csv

## Running Application

Preprocess the data and generate recommendations
```bash
python generate_recommendations.py
```

Start the flask application 
```bash
python app.py
```

Open your browser and go to http://127.0.0.1:5000/ to access the application.

## Usage

* Homepage: Enter your skin type to receive personalized skincare product recommendations.
* Recommendations: The system will display the top 5 product recommendations based on your skin type.

## Detailed Workflow

1. Data Preprocessing:

* Merge product information and reviews data.
* Sample a subset of data for efficiency.

2. Recommendation System:

* Hybrid Approach: Combines content-based, collaborative filtering, and sentiment analysis methods.
* Content-Based Filtering: Utilizes TF-IDF vectorization and cosine similarity.
* Collaborative Filtering: Uses user-item interaction matrix and cosine similarity.
* Sentiment Analysis: Analyzes reviews to filter products based on sentiment towards specific skin types.

3. Frontend
 * Simple HTML interface to input user skin type and display recommendations.

## License
This project is licensed under the MIT License.