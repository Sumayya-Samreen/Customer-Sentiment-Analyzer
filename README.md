
# Customer Sentiment Analyzer

Customer Sentiment Analyzer is an interactive Streamlit application that transforms raw CSV datasets into insightful visualizations using natural language processing and sentiment analysis. It enables real-time exploration of customer sentiment, dynamic word clouds, and interactive dashboards to uncover trends and actionable insights.

## Features

- CSV Upload: Upload and preview datasets instantly.
- Custom Analysis: Select specific columns for targeted sentiment and word cloud generation.
- WordCloud Visualization: Dynamic word clouds with stopword removal and lemmatization.
- Sentiment Analysis: Real-time sentiment scoring with VaderSentiment.
- Interactive Charts: Visualize sentiment scores using Plotly.
- Downloadable Reports: Export sentiment summaries as CSV files.
- User-Friendly Interface: Easy-to-use Streamlit UI requiring no coding.

## Installation

\`\`\`bash
git clone https://github.com/<your-username>/Customer-Sentiment-Analyzer.git
cd Customer-Sentiment-Analyzer
python -m venv .venv
# Activate venv:
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
streamlit run Customer_Sentiment_Analyzer.py
\`\`\`

## Technologies & Libraries

- Streamlit — Interactive web app deployment
- NLTK — Natural language processing
- WordCloud — Text visualization
- VaderSentiment — Sentiment scoring
- Matplotlib & Plotly — Data visualization
- Pandas — Data manipulation

## Pro Tip for Recruiters / Collaborators

This project exemplifies a complete machine learning and data visualization workflow — from data preprocessing and NLP feature engineering to interactive deployment via Streamlit. It highlights expertise in text processing, sentiment analysis, data visualization, and deployment readiness, making it a strong portfolio piece for roles in machine learning, data science, and AI engineering.

## Author

**Sumayya Samreen — M.Sc. in Artificial Intelligence**
Passionate about applied AI, model interpretability, and building real-world machine learning solutions.
