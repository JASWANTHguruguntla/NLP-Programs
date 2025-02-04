import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
def analyze_sentiment(text):
    sia=SentimentIntensityAnalyzer()
    sentiment_scores=sia.polarity_scores(text)
    if sentiment_scores['compound']>=0.05:
        return 'positive'
    elif sentiment_scores['compound']<=-0.05:
        return 'negative'
    else:
        return 'neutral'
text="I run working with python! it's such a powerful language."
result=analyze_sentiment(text)
print(f"sentiment:{result}")
