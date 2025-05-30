#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class DescriptiveStats:
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
        articles_per_day = self.df.groupby(date_column).size()
        plt.figure(figsize=(10, 6))
        articles_per_day.plot(kind='line')
        plt.title('Number of Articles Published Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.show()
    def plot_publication_weekly_trends(self, date_column):
        self.df['day_of_week'] = self.df[date_column].dt.day_name()
        articles_by_day = self.df['day_of_week'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        plt.figure(figsize=(10, 6))
        articles_by_day.plot(kind='bar')
        plt.title('Number of Articles by Day of the Week')
        plt.xlabel('Day of the Week')
        plt.ylabel('Number of Articles')
        plt.show()

    def plot_articles_per_publisher(self, publisher_column):
        """        Plots the number of articles per publisher.
        Args:
            publisher_column (str): The name of the column containing publisher information.
        """

        if publisher_column not in self.df.columns:
            raise ValueError(f"Column '{publisher_column}' does not exist in the DataFrame.")

        articles_per_publisher = self.get_articles_per_publisher(publisher_column)
        articles_per_publisher.plot(kind='bar')
        plt.title('Articles per Publisher')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.show()
    def plot_text_length_distribution(self, text_column):
        """
        Plots the distribution of text lengths in a specified column.
        Args:
            text_column (str): The name of the column containing text data.
        """
        if text_column not in self.df.columns:
            raise ValueError(f"Column '{text_column}' does not exist in the DataFrame.")

        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[text_column].apply(lambda x: len(str(x))), bins=30, color='blue', alpha=0.7)
        plt.title(f'Distribution of {text_column} Lengths')
        plt.xlabel(f'{text_column} Length')
        plt.ylabel('Frequency')
        plt.show()