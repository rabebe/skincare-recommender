import pandas as pd
import re


def load_data(file_path):
    try:
        df = pd.read_csv(file_path, low_memory=False)
        return df
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

def preprocess_data(df):
    # Perform any preprocessing steps here (e.g., handling missing values, data cleaning, feature engineering)
    # Example: Remove rows with missing values
    df['review_text'] = df['review_text'].fillna("")
    df['highlights'] = df['highlights'].fillna("")
    df['skin_type'] = df['skin_type'].fillna("")
    return df

def merge_data(file1_path, file2_path, on_column):
    df1 = load_data(file1_path)
    df2 = load_data(file2_path)
    
    if df1 is not None and df2 is not None:
        merged_df = pd.merge(df1, df2, on=on_column)
        preprocessed_df = preprocess_data(merged_df)
        return preprocessed_df
    else:
        print("Error loading files. Ensure both file paths are correct.")
        return None

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text




