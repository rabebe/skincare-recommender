from content_based import recommend_content_based
from collaborative_filtering import collaborative_filtering
from sentiment_analysis import filter_based_on_user_skin_type

def hybrid_recommendation_system(df, user_skin_type, top_n=5, max_samples=None):
    """
    Generate hybrid recommendations by combining multiple recommendation methods.

    Args:
    df (DataFrame): The dataframe containing product data.
    user_skin_type (str): The user's skin type for filtering relevant products.
    top_n (int): Number of top recommendations to return.
    max_samples (int): Maximum number of samples to consider for content-based filtering.

    Returns:
    list: A list of hybrid recommendations.
    """

    # Generate recommendations using content-based filtering
    content_based_recommendations = recommend_content_based(df, user_skin_type, top_n, max_samples)

    # Generate recommendations using collaborative filtering
    collaborative_recommendations = collaborative_filtering(df, user_skin_type, top_n)
    
    # Generate recommendations using sentiment-based filtering
    sentiment_based_recommendations = filter_based_on_user_skin_type(df, user_skin_type, top_n)
    
    # Combine recommendations from all methods into a set to ensure uniqueness
    combined_recommendations = set(content_based_recommendations + collaborative_recommendations + sentiment_based_recommendations)
    
    return list(combined_recommendations)[:top_n]