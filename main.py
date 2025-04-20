from scripts.load_data import load_tickets
from scripts.preprocess import preprocess_text
from scripts.analyze_tickets import analyze_tickets
from scripts.generate_report import generate_report
from scripts.group_report import generate_group_report

import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']  # Compound score represents overall sentiment

def analyze_tickets(processed_texts):
    # Sentiment analysis
    sentiment_scores = processed_texts.apply(analyze_sentiment)
    sentiment_summary = sentiment_scores.describe()  # Provides summary statistics (e.g., mean, std, min, max)

    # For a more detailed sentiment categorization, you can use:
    sentiment_categories = processed_texts.apply(lambda text: 'Positive' if analyze_sentiment(text) > 0.2 else 
                                                ('Negative' if analyze_sentiment(text) < -0.2 else 'Neutral'))

    sentiment_count = sentiment_categories.value_counts()  # Count of each sentiment category (Positive, Neutral, Negative)

    # Keyword frequency (this would be the "summary" you're passing to generate_report)
    from collections import Counter
    all_keywords = ' '.join(processed_texts).split()
    keyword_frequency = Counter(all_keywords).most_common(20)  # Get the top 20 most frequent words
    
    return keyword_frequency, sentiment_count, sentiment_summary  # Return both

def main():
    # Load & preprocess
    df = load_tickets("data/customer_support_tickets.csv")
    df["processed_text"] = df["Ticket Description"].apply(preprocess_text)
    os.makedirs("output", exist_ok=True)

    # Perform sentiment analysis and keyword frequency analysis
    keyword_summary, sentiment_categories, sentiment_summary = analyze_tickets(df["processed_text"])

    # Overall report + chart (including sentiment analysis)
    generate_report(keyword_summary, "output/summary_report.txt", sentiment_summary, sentiment_categories)

    # Grouped reports
    generate_group_report(df, "Product Purchased", "processed_text", top_n=10)
    generate_group_report(df, "Ticket Priority",    "processed_text", top_n=10)

if __name__ == "__main__":
    main()
