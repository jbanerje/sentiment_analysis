from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiments(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)

    if score['compound'] >= 0.05 :
        return 'Positive Sentiment', score
    elif ( score['compound'] > -0.05 and score['compound'] < 0.05 ):
        return 'Neutral Sentiment', score
    else:
        return 'Negative Sentiment', score