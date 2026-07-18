# Sentiment Dashboard

A Streamlit app for scoring one text sample or a batch of tweet export rows.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Xquik Or TweetClaw Export Workflow

Use the **Xquik Export** tab to upload reviewed
[Xquik](https://github.com/Xquik-dev/x-twitter-scraper) or
[TweetClaw](https://github.com/Xquik-dev/tweetclaw) data. CSV, JSON, JSONL, and
NDJSON files are supported.

The app looks for one of these text columns:

- `text`
- `content`
- `tweet_text`
- `full_text`
- `body`

After scoring, use **Download scored CSV** to save the original rows with a
new `sentiment` column.

Non-text and missing values in the selected text column are treated as neutral
while their original values remain in the downloaded data.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
