# 🛠️ Customer Support Ticket Analysis

This project analyzes customer support tickets to identify key issues, group trends, and sentiment using Natural Language Processing (NLP).

## 📌 Project Structure

customer_support_analysis/
├── data/
│   └── customer_support_tickets.csv      # Input ticket data
│
├── output/
│   ├── summary_report.txt                # Overall top keywords
│   ├── top_keywords.png                  # Visual of top keywords
│   ├── by_product_purchased.txt          # Keyword summary by product
│   ├── by_ticket_priority.txt            # Keyword summary by priority
│   └── sentiment_distribution.png        # Sentiment analysis chart
│
├── scripts/
│   ├── load_data.py                      # Loads the CSV data
│   ├── preprocess.py                     # Text cleaning & tokenization
│   ├── analyze_tickets.py                # Keyword & sentiment analysis
│   ├── group_report.py                   # Grouped analysis & export
│   └── generate_report.py                # Final report + chart generation
│
├── main.py                               # Main runner script
├── requirements.txt                      # Python dependencies
└── README.md                             # Project documentation (this file)


## 🧪 Features

- Cleans and tokenizes support ticket text
- Extracts top frequent keywords
- Groups keywords by:
- Product Purchased 
- Ticket Priority
- Performs sentiment analysis (Positive / Neutral / Negative)
- Generates visual charts (`.png`) and text summaries (`.txt`)

## 🚀 How to Run

1. "Install Dependencies"
bash
   pip install -r requirements.txt

## Run the Analysis

python main.py

## Check Results

Open the output/ folder for reports and graphs

## 🧠Tools Used

1)Python
2)NLTK
3)Matplotlib
4)VADER Sentiment (from vaderSentiment)

## 📈Output Examples

- top_keywords.png — most common issues
- sentiment_distribution.png — positive vs. negative ticket tone
- by_product_purchased.txt — top keywords per product
- summary_report.txt — global keyword summary

## ✅ Task Coverage

-Preprocessing
-Keyword Frequency
-Grouped Analysis
-Sentiment Analysis
-Visualizations

## 📌 Note

You only need to run main.py — all other scripts are modular and automatically called from it.

## ✍️ Author
Shashank 💻