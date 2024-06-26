import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def collaborative_filtering(df, user_skin_type, top_n=5):
    """
    Recommend products using collaborative filtering based on user ratings.

    Args:
    df (DataFrame): The dataframe containing product and rating data.
    user_skin_type (str): The user's skin type for filtering relevant products.
    top_n (int): Number of top recommendations to return.

    Returns:
    list: A list of recommended product names.
    """

    # Filter the dataframe to include only products relevant to the user's skin type
    df_filtered = df[df['skin_type'].str.lower().str.contains(user_skin_type.lower())]
    
    # Create a user-item matrix where rows are users and columns are products with ratings
    user_item_matrix = df_filtered.pivot_table(index='author_id', columns='product_id', values='rating_x').fillna(0)
    
    # Compute the cosine similarity between users based on their ratings
    user_similarity = cosine_similarity(user_item_matrix)

    # Fill the diagonal with zeros to exclude self-similarity
    np.fill_diagonal(user_similarity, 0)
    
    # Convert the user similarity matrix to a DataFrame for easier manipulation
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    
    # Calculate weighted ratings for each product by dot product of user similarity and user item matrix
    # then normalize by the sum of similarities
    weighted_ratings = user_similarity_df.dot(user_item_matrix) / user_similarity_df.sum(axis=1).replace(0, np.nan)

    # Get the indices of top N products with the highest average weighted ratings
    top_recommendations = weighted_ratings.mean().nlargest(top_n).index
    
    # Retrieve the names of the recommended products based on the indices
    recommended_products = df_filtered[df_filtered['product_id'].isin(top_recommendations)]
    return recommended_products['product_name_x'].tolist()
