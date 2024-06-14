from content_based import recommend_content_based
from collaborative_filtering import collaborative_filtering
from sentiment_analysis import filter_based_on_user_skin_type

def hybrid_recommendation_system(df, user_skin_type, top_n=5, max_samples=None):
    content_based_recommendations = recommend_content_based(df, user_skin_type, top_n, max_samples)
    collaborative_recommendations = collaborative_filtering(df, user_skin_type, top_n)
    sentiment_based_recommendations = filter_based_on_user_skin_type(df, user_skin_type, top_n)

    combined_recommendations = set(content_based_recommendations + collaborative_recommendations + sentiment_based_recommendations)
    return list(combined_recommendations)[:top_n]
