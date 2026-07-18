import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


def detect_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    if compound >= 0.05:
        return "Positive"
    if compound <= -0.05:
        return "Negative"
    return "Neutral"


def score_frame(frame, column):
    result = frame.copy()
    normalized_text = result[column].map(lambda value: value if isinstance(value, str) else "")
    result["sentiment"] = normalized_text.map(detect_sentiment)
    return result
