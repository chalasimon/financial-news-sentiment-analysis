# import libraries
import pandas as pd
import nltk
from sklearn.decomposition import LatentDirichletAllocation
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
class TextAnalysis:
    """
    A class for performing text analysis on a DataFrame containing news articles.
    Use natural language processing to identify common keywords or phrases, potentially extracting topics or significant events (like "FDA approval", "price target", etc.).
    
    Attributes:
        df (pd.DataFrame): The DataFrame containing the news articles.
    """
    
    def __init__(self, df):
        self.df = df
        self.sia = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text):

        score=self.sia.polarity_scores(text)
        if score['compound']>0:
            sentiment='Positive'
        elif score['compound']<0:
            sentiment='Negative'
        else:
            sentiment='Neutral'
        return score['compound'], sentiment
    def preprocess_text(self, headline_text):
       headline_text = headline_text.lower()
       headline_text = nltk.RegexpTokenizer(r"\w+").tokenize(headline_text)
       stopwords = nltk.corpus.stopwords.words('english')
       headline_text = [word for word in headline_text if word not in stopwords]
       return ' '.join(headline_text)

    def top_words(self, df, num_words=5):
        # vectorize the text
        self.df = df
        vectorizer = CountVectorizer(max_features=1000)
        X = vectorizer.fit_transform(self.df['processed_headline'])

        # Fit LDA model
        lda = LatentDirichletAllocation(n_components=5, random_state=0)
        lda.fit(X)

        # Get topic terms
        feature_names = vectorizer.get_feature_names_out()
        topics = lda.components_

        # Display top words per topic
        num_words = 10
        for topic_idx, topic in enumerate(topics):
            print(f"Topic #{topic_idx + 1}:")
            print(" ".join([feature_names[i] for i in topic.argsort()[:-num_words - 1:-1]]))
            print()
    
   