import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from preprocessing import preprocess_text

def recommend_content_based(df, user_skin_type, top_n=5, max_samples=None):
    df['processed_highlights'] = df['highlights'].apply(preprocess_text)
    df_filtered = df[df['skin_type'].str.lower().str.contains(user_skin_type.lower())]
    if max_samples is not None:
        df_filtered = df_filtered.sample(min(len(df_filtered), max_samples))
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_filtered['processed_highlights'])
    similarity_scores = linear_kernel(tfidf_matrix, tfidf_matrix)
    top_indices = similarity_scores.argsort(axis=1)[:, ::-1][:top_n].flatten()
    recommended_products = df_filtered.iloc[top_indices]['product_name_x']
    return recommended_products.tolist()
