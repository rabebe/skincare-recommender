import pandas as pd
import re


def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame or None: Loaded DataFrame if the file exists, otherwise None.
    """
    try:
        df = pd.read_csv(file_path, low_memory=False)
        return df
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

def preprocess_data(df):
    """
    Preprocess the DataFrame by handling missing values and other cleaning tasks.

    Args:
    df (DataFrame): The DataFrame to preprocess.

    Returns:
    DataFrame: The preprocessed DataFrame.
    """
    # Fill missing values in specific columns with empty strings
    df['review_text'] = df['review_text'].fillna("")
    df['highlights'] = df['highlights'].fillna("")
    df['skin_type'] = df['skin_type'].fillna("")
    return df

def merge_data(file1_path, file2_path, on_column):
    """
    Merge two CSV files on a specified column and preprocess the resulting DataFrame.

    Args:
    file1_path (str): Path to the first CSV file.
    file2_path (str): Path to the second CSV file.
    on_column (str): The column name to merge the files on.

    Returns:
    DataFrame or None: The merged and preprocessed DataFrame, or None if there was an error.
    """
    # Load data from the provided file paths
    df1 = load_data(file1_path)
    df2 = load_data(file2_path)
    
    # Check if both dataframes are loaded successfully, merge the dataframes and preprocess the merged dataframe
    if df1 is not None and df2 is not None:
        merged_df = pd.merge(df1, df2, on=on_column)
        preprocessed_df = preprocess_data(merged_df)
        return preprocessed_df
    else:
        print("Error loading files. Ensure both file paths are correct.")
        return None

def preprocess_text(text):
    """
    Preprocess a text string by converting to lowercase and removing punctuation.

    Args:
    text (str): The text string to preprocess.

    Returns:
    str: The preprocessed text string.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text