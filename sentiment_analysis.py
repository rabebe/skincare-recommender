from textblob import TextBlob
from preprocessing import preprocess_text

def analyze_sentiment(review):
    """
    Analyze the sentiment polarity of a given review text using TextBlob.

    Args:
    review (str): The review text to analyze.

    Returns:
    float: The sentiment polarity score (-1 to 1).
    """
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

def filter_based_on_user_skin_type(df, user_skin_type, top_n=5):
    """
    Filter products based on user's skin type and positive sentiment reviews.

    Args:
    df (DataFrame): The dataframe containing product data.
    user_skin_type (str): The user's skin type for filtering relevant products.
    top_n (int): Number of top recommendations to return.

    Returns:
    list: A list of product names recommended based on user's skin type and positive sentiment.
    """
    processed_skin_type = preprocess_text(user_skin_type)
    filtered_df = df[df['skin_type'].str.lower().str.contains(processed_skin_type)]
    
    # Filter positive sentiment reviews and select unique product names
    filtered_df['sentiment'] = filtered_df['review_text'].apply(analyze_sentiment)
    positive_reviews_df = filtered_df[filtered_df['sentiment'] > 0]
    return positive_reviews_df.drop_duplicates(subset='product_name_x').head(top_n)['product_name_x'].tolist()
