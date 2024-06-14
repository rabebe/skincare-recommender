from textblob import TextBlob
from preprocessing import preprocess_text

def analyze_sentiment(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

def filter_based_on_user_skin_type(df, user_skin_type, top_n=5):
    processed_skin_type = preprocess_text(user_skin_type)
    filtered_df = df[df['skin_type'].str.lower().str.contains(processed_skin_type)]
    filtered_df['sentiment'] = filtered_df['review_text'].apply(analyze_sentiment)
    positive_reviews_df = filtered_df[filtered_df['sentiment'] > 0]
    return positive_reviews_df.drop_duplicates(subset='product_name_x').head(top_n)['product_name_x'].tolist()
