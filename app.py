import json
from pathlib import Path

import pandas as pd
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


TEXT_COLUMNS = ("text", "content", "tweet_text", "full_text", "body")


st.set_page_config(page_title="Sentiment Dashboard", layout="wide")
st.title("Sentiment Dashboard")

analyzer = SentimentIntensityAnalyzer()


def detect_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    if compound >= 0.05:
        return "Positive"
    if compound <= -0.05:
        return "Negative"
    return "Neutral"


def text_column(frame):
    for column in TEXT_COLUMNS:
        if column in frame.columns:
            return column
    return None


def load_uploaded_file(uploaded_file):
    suffix = Path(uploaded_file.name).suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(uploaded_file)

    payload = uploaded_file.getvalue().decode("utf-8-sig").strip()
    if suffix in {".jsonl", ".ndjson"}:
        rows = [json.loads(line) for line in payload.splitlines() if line.strip()]
        return pd.DataFrame(rows)

    parsed = json.loads(payload)
    if isinstance(parsed, dict):
        for key in ("tweets", "data", "items", "results"):
            if isinstance(parsed.get(key), list):
                return pd.DataFrame(parsed[key])
    return pd.DataFrame(parsed)


tab_single, tab_batch = st.tabs(["Single Text", "Xquik Export"])

with tab_single:
    text = st.text_input("Enter text")
    if st.button("Analyze"):
        if not text.strip():
            st.warning("Enter text first.")
        else:
            sentiment = detect_sentiment(text)
            if sentiment == "Positive":
                st.success("Positive")
            elif sentiment == "Negative":
                st.error("Negative")
            else:
                st.info("Neutral")

with tab_batch:
    st.caption("Upload a reviewed Xquik or TweetClaw CSV, JSON, JSONL, or NDJSON export.")
    uploaded = st.file_uploader(
        "Tweet export",
        type=["csv", "json", "jsonl", "ndjson"],
    )

    if uploaded is not None:
        try:
            frame = load_uploaded_file(uploaded)
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as error:
            st.error(f"Could not read file: {error}")
        else:
            column = text_column(frame)
            if column is None:
                st.error("Add a text, content, tweet_text, full_text, or body column.")
            else:
                result = frame.copy()
                result["sentiment"] = result[column].fillna("").map(detect_sentiment)
                st.dataframe(result[[column, "sentiment"]], use_container_width=True)
                summary = result["sentiment"].value_counts().rename_axis("sentiment")
                st.bar_chart(summary)
                st.download_button(
                    "Download scored CSV",
                    result.to_csv(index=False).encode("utf-8"),
                    "xquik-sentiment.csv",
                    "text/csv",
                )
