import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st

nltk.download('vader_lexicon')

def analyze_text(df):
    text_cols = df.select_dtypes(include='object').columns
    if text_cols.any():
        sia = SentimentIntensityAnalyzer()
        st.subheader("Text Analysis")
        for col in text_cols:
            sentiments = df[col].dropna().apply(lambda x: sia.polarity_scores(x)['compound'])
            st.write(f"Sentiment scores for {col}:")
            st.line_chart(sentiments)
