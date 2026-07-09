# Sentiment Dashboard

A Streamlit app for scoring one text sample or a batch of tweet export rows.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Xquik Or TweetClaw Export Workflow

Use the **Xquik Export** tab to upload a reviewed Xquik or TweetClaw export.
CSV, JSON, JSONL, and NDJSON files are supported.

The app looks for one of these text columns:

- `text`
- `content`
- `tweet_text`
- `full_text`
- `body`

After scoring, use **Download scored CSV** to save the original rows with a
new `sentiment` column.
