from collections import Counter
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']

def top_keywords_by_group(df, group_col, text_col, top_n=10):
    """
    Returns a dict mapping each unique value in `group_col`
    to its list of top_n (word, freq) pairs from `text_col`.
    """
    result = {}
    for group_val, subdf in df.groupby(group_col):
        all_words = " ".join(subdf[text_col]).split()
        result[group_val] = Counter(all_words).most_common(top_n)
    return result

def generate_group_report(df, group_col, text_col, top_n=10, output_dir="output"):
    """
    Write a text file listing the top N keywords for each group in `group_col`.
    """
    os.makedirs(output_dir, exist_ok=True)
    group_keywords = top_keywords_by_group(df, group_col, text_col, top_n)
    
    # e.g. output/by_product_purchased.txt or by_ticket_priority.txt
    filename = f"by_{group_col.replace(' ', '_').lower()}.txt"
    report_path = os.path.join(output_dir, filename)
    
    with open(report_path, "w") as f:
        f.write(f"Top {top_n} keywords by {group_col}:\n\n")
        for group_val, keywords in group_keywords.items():
            f.write(f"{group_val}:\n")
            for word, freq in keywords:
                f.write(f"  {word}: {freq}\n")
            f.write("\n")
    
    print(f"✅ Group report for '{group_col}' written to: {report_path}")
