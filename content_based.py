import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from preprocessing import preprocess_text

def recommend_content_based(df, user_skin_type, top_n=5, max_samples=None):
    """
    Recommend products based on content similarity.
    
    Args:
    df (DataFrame): The dataframe containing product data.
    user_skin_type (str): The user's skin type for filtering relevant products.
    top_n (int): Number of top recommendations to return.
    max_samples (int): Maximum number of samples to consider for efficiency.
    
    Returns:
    list: A list of recommended product names.
    """
    # Preprocess the 'highlights' text for each product
    df['processed_highlights'] = df['highlights'].apply(preprocess_text)

    # Filter the dataframe to include only products relevant to user's skin type
    df_filtered = df[df['skin_type'].str.lower().str.contains(user_skin_type.lower())]
    
    # If max_samples is specified, sample a subset of the filtered data
    if max_samples is not None:
        df_filtered = df_filtered.sample(min(len(df_filtered), max_samples))
    
    # Create a TF-IDF vectorizer and transform the processed highlights text
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_filtered['processed_highlights'])
    
    # Computer similarity scores between products
    similarity_scores = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # Get indices of the top N most similar products
    top_indices = similarity_scores.argsort(axis=1)[:, ::-1][:top_n].flatten()
    
    # Retrieve the names of the recommended products based on the indices
    recommended_products = df_filtered.iloc[top_indices]['product_name_x']
    
    return recommended_products.tolist()