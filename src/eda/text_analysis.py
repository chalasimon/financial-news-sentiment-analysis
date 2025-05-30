# import libraries
import pandas as pd
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.sentiment import SentimentIntensityAnalyzer
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
    
    def extract_keywords(self, text_column, num_keywords=10):
        """        Extracts the most common keywords from the text in a specified column.
        Args:
            text_column (str): The name of the column containing text data.
            num_keywords (int): The number of top keywords to return.

        Returns:
            pd.Series: A Series containing the most common keywords.
        """
        if text_column not in self.df.columns:
            raise ValueError(f"Column '{text_column}' does not exist in the DataFrame.")

        # Tokenize the text and extract keywords
        keywords = self.df[text_column].str.cat(sep=' ').split()
        keywords = pd.Series(keywords).value_counts().head(num_keywords)
        return keywords
    
    def topic_distribution(self, text_column):
        """
        Analyzes the distribution of topics in the text data.
        Args:
            text_column (str): The name of the column containing text data.
        Returns:
            pd.Series: A Series containing the distribution of topics.
        """
        if text_column not in self.df.columns:
            raise ValueError(f"Column '{text_column}' does not exist in the DataFrame.")

        # Tokenize the text and count occurrences of each word
        words = self.df[text_column].str.cat(sep=' ').split()
        topic_distribution = pd.Series(words).value_counts()
        return topic_distribution