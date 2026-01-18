
# Customer Sentiment Analyzer

## Description
Customer Sentiment Analyzer is an interactive Streamlit application that enables users to upload CSV files and instantly visualize sentiment analysis results along with enhanced WordClouds. It leverages NLP techniques, text preprocessing, and data visualization to deliver actionable insights from textual datasets.

## Features
- Upload CSV files for analysis  
- Dynamic selection of columns for sentiment analysis and WordCloud generation  
- NLP preprocessing including lemmatization and stopword removal  
- Interactive WordCloud visualizations  
- Sentiment analysis using VADER  
- Interactive sentiment score plots with Plotly  
- Downloadable sentiment analysis summary CSV  
- Responsive Streamlit-based interface

## Installation

Follow these steps to set up and run the Customer Sentiment Analyzer locally:

```bash
# 1. Clone the repository
git clone https://github.com/Sumayya-Samreen/Customer-Sentiment-Analyzer.git

# 2. Change to the project directory
cd Customer-Sentiment-Analyzer

# 3. Create a virtual environment
python -m venv .venv
```

### Activate the virtual environment

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
streamlit run Customer_Sentiment_Analyzer.py
```

## Live Demo
Try it here: https://customer-sentiment-analyzer-25.streamlit.app/

## Usage
1. Upload your CSV file containing textual data.
2. Select columns for analysis in the sidebar.
3. View generated WordClouds and sentiment scores.
4. Download the sentiment summary CSV.

## Pro Tip for Recruiters / Collaborators
This project exemplifies a complete machine learning and data visualization workflow; from data preprocessing and feature engineering to model development, evaluation, and deployment readiness. It highlights expertise in text processing, sentiment analysis, data visualization, and deployment readiness, making it a strong portfolio piece for roles in machine learning, data science, and AI engineering.

## Author
**Sumayya Samreen — M.Sc. in Artificial Intelligence**<br>
Focused on applied NLP, interpretable analytics, and production-grade AI solutions.