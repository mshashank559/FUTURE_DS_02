import matplotlib.pyplot as plt

def generate_report(keyword_summary, output_file, sentiment_summary=None, sentiment_categories=None):
    # Write the keyword frequency summary to a text file
    with open(output_file, "w") as f:
        f.write("Top Frequently Reported Issues:\n")
        for word, count in keyword_summary:
            f.write(f"{word}: {count}\n")
        
        # Write sentiment analysis summary if available
        if sentiment_summary is not None:
            f.write("\nSentiment Summary:\n")
            f.write(f"Sentiment Overview (Mean Score, Min, Max, etc.):\n")
            f.write(f"{sentiment_summary}\n")

        # Sentiment Categories (Positive, Negative, Neutral)
        if sentiment_categories is not None:
            f.write("\nSentiment Distribution:\n")
            for sentiment, count in sentiment_categories.items():
                f.write(f"{sentiment}: {count}\n")

    # Visualization of the top keywords
    words, counts = zip(*keyword_summary)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.xticks(rotation=90)
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.title('Top 20 Frequently Reported Issues')
    plt.tight_layout()
    plt.savefig('output/top_keywords.png')
    plt.show()

    # Visualization of Sentiment Distribution
    if sentiment_categories is not None:
        sentiment_labels = sentiment_categories.index
        sentiment_values = sentiment_categories.values
        plt.figure(figsize=(8, 6))
        plt.bar(sentiment_labels, sentiment_values, color=['green', 'gray', 'red'])
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.title('Sentiment Distribution')
        plt.tight_layout()
        plt.savefig('output/sentiment_distribution.png')
        plt.show()
