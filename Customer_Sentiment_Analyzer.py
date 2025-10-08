import streamlit as st
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
from wordcloud import WordCloud, STOPWORDS 
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt 
import pandas as pd
import os
import plotly.express as px
from nltk.corpus import stopwords as nltk_stopwords

# Streamlit App 
st.set_page_config(page_title="Customer Sentiment Analyzer", layout="wide")

st.title("Customer Sentiment Analyzer")
st.markdown("Upload your CSV and instantly visualize enhanced WordClouds and Sentiment Analysis results.")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        st.stop()

    st.success("CSV Loaded Successfully!")
    st.write("Preview of your data:", df.head())

    # Sidebar settings
    st.sidebar.header("Settings")
    selected_categories = st.sidebar.multiselect(
        "Select categories for WordCloud and Sentiment Analysis",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

    lemmatizer = WordNetLemmatizer()
    custom_stopwords = set(STOPWORDS).union(set(nltk_stopwords.words("english")))
    custom_stopwords.add("product")

    def generate_wordcloud(text_series, title):
        comment_words = " ".join(
            lemmatizer.lemmatize(str(word).lower()) 
            for word in text_series if isinstance(word, str)
        )

        wordcloud = WordCloud(
            width=800, height=800,
            background_color='white',
            stopwords=custom_stopwords,
            min_font_size=10
        ).generate(comment_words)

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        plt.title(title, fontsize=16)
        st.pyplot(fig)

    st.header("WordClouds by Selected Categories")
    for category in selected_categories:
        st.subheader(f"Category: {category}")
        generate_wordcloud(df[category], f"WordCloud for {category}")

    # Sentiment Analysis
    st.header("Sentiment Analysis by Category")
    sid = SentimentIntensityAnalyzer()
    sentiment_results = {}

    for col in selected_categories:
        text = " ".join(df[col].astype(str))
        sentiment_results[col] = sid.polarity_scores(text)

    df_sentiments = pd.DataFrame(sentiment_results).T
    df_sentiments.index.name = "Category"
    st.write(df_sentiments)

    # Interactive sentiment plot
    fig = px.bar(
        df_sentiments.reset_index(),
        x="Category", y=["neg", "neu", "pos"],
        title="Sentiment Scores by Feature Category",
        barmode="group", height=500
    )
    st.plotly_chart(fig)

    # Download sentiment results
    df_sentiments.to_csv("sentiment_summary.csv")
    st.download_button("Download Sentiment Summary CSV", "sentiment_summary.csv", "sentiment_summary.csv")

    # Overall sentiment summary
    st.header("Overall Sentiment Summary")
    summary_text = []
    for category_name, scores in sentiment_results.items():
        compound = scores["compound"]
        overall = "positive" if compound >= 0.05 else "negative" if compound <= -0.05 else "neutral"
        summary_text.append(f"{category_name} — {overall}")

    st.markdown("\n".join(summary_text))

else:
    st.info("Upload a CSV file to get started.")
