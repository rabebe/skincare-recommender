import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def collaborative_filtering(df, user_skin_type, top_n=5):
    df_filtered = df[df['skin_type'].str.lower().str.contains(user_skin_type.lower())]
    user_item_matrix = df_filtered.pivot_table(index='author_id', columns='product_id', values='rating_x').fillna(0)
    user_similarity = cosine_similarity(user_item_matrix)
    np.fill_diagonal(user_similarity, 0)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    weighted_ratings = user_similarity_df.dot(user_item_matrix) / user_similarity_df.sum(axis=1).replace(0, np.nan)
    top_recommendations = weighted_ratings.mean().nlargest(top_n).index
    recommended_products = df_filtered[df_filtered['product_id'].isin(top_recommendations)]
    return recommended_products['product_name_x'].tolist()
