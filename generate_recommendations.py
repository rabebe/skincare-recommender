import pandas as pd
from preprocessing import merge_data
from hybrid import hybrid_recommendation_system

# File paths for the data
file1_path = "data/product_info.csv"
file2_path = "data/reviews_0-250.csv"
on_column = "product_id"

# Preprocess data by merging product info and reviews on product id
preprocessed_df = merge_data(file1_path, file2_path, on_column)

# Get user input for skin type
user_skin_type = input("Enter your skin type (e.g., combination, oily, dry): ")

# Sample a subset of the data for efficiency
preprocessed_df = preprocessed_df.sample(10000, random_state=42)

# Generate recommendations based on user's skin type
recommendations = hybrid_recommendation_system(preprocessed_df, user_skin_type)

print(recommendations)