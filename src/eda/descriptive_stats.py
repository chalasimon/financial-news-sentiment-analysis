#import libraries
import pandas as pd
import numpy as np
class Descriptive:
    '''
       - Obtain basic statistics for textual lengths (like headline length).
       - Count the number of articles per publisher to identify which publishers are most active.
       - Analyze the publication dates to see trends over time, such as increased news frequency on particular days or during specific events.
    '''
    def __init__(self, df):
        self.df = df

    def get_descriptive_stats(self):
        """
        Returns descriptive statistics for the DataFrame.
        """
        return self.df.describe()

    def get_missing_values(self):
        """
        Returns the count of missing values in each column.
        """
        return self.df.isnull().sum()

    def get_unique_values(self):
        """
        Returns the count of unique values in each column.
        """
        return self.df.nunique()
    def get_text_length_stats(self, text_column):
        """
        Returns basic statistics for the lengths of text in a specified column.
        Args:
            text_column (str): The name of the column containing text data.
        Returns:
            pd.Series: A Series containing the length of each text entry.
        """
        if text_column not in self.df.columns:
            raise ValueError(f"Column '{text_column}' does not exist in the DataFrame.")
        
        text_lengths = self.df[text_column].apply(lambda x: len(str(x)))
        return text_lengths.describe()
    def get_articles_per_publisher(self, publisher_column):
        """
        Returns the count of articles for each publisher.
        Args:
            publisher_column (str): The name of the column containing publisher information.
        Returns:
            pd.Series: A Series containing the count of articles per publisher.
        """
        if publisher_column not in self.df.columns:
            raise ValueError(f"Column '{publisher_column}' does not exist in the DataFrame.")

        return self.df[publisher_column].value_counts()
    def get_publication_date_trends(self, date_column):
        """
        Returns the trends in publication dates over time.
        Args:
            date_column (str): The name of the column containing publication date information.
        Returns:
            pd.Series: A Series containing the count of articles published on each date.
        """
        if date_column not in self.df.columns:
            raise ValueError(f"Column '{date_column}' does not exist in the DataFrame.")
        return self.df[date_column].value_counts()