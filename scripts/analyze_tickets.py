from collections import Counter
import nltk

# Analyze ticket text and return a summary
def analyze_tickets(processed_text_column):
    all_words = " ".join(processed_text_column).split()
    word_count = Counter(all_words)
    
    # Return most common 20 words as summary
    top_keywords = word_count.most_common(20)
    return top_keywords
