import unittest

import pandas as pd

from sentiment import detect_sentiment, score_frame


class SentimentTest(unittest.TestCase):
    def test_detect_sentiment_covers_all_labels(self):
        self.assertEqual(detect_sentiment("I love this"), "Positive")
        self.assertEqual(detect_sentiment("I hate this"), "Negative")
        self.assertEqual(detect_sentiment("This is a table"), "Neutral")

    def test_score_frame_normalizes_non_text_cells(self):
        frame = pd.DataFrame({"text": [123, 3.14, True, None, "good", "bad"]})

        result = score_frame(frame, "text")

        self.assertEqual(
            result["sentiment"].tolist(),
            ["Neutral", "Neutral", "Neutral", "Neutral", "Positive", "Negative"],
        )
        self.assertEqual(result["text"].tolist()[:3], [123, 3.14, True])


if __name__ == "__main__":
    unittest.main()
