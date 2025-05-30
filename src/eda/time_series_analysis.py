# src/eda/time_series_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TimeSeriesAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.df['date'] = pd.to_datetime(self.df['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')
        self.df['publication_date'] = self.df['date'].dt.date
        self.articles_per_day = self.df.groupby('publication_date').size()
        self.articles_by_hour = None

    def plot_articles_over_time(self):
        """Plot number of articles published per day."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.articles_per_day, label='Number of Articles per Day', color='blue')
        plt.title('Number of Articles Published Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_rolling_mean(self, window=7):
        """Plot rolling mean to identify spikes in publication frequency."""
        rolling_mean = self.articles_per_day.rolling(window=window).mean()
        plt.figure(figsize=(12, 6))
        plt.plot(self.articles_per_day, label='Number of Articles per Day', color='blue', alpha=0.5)
        plt.plot(rolling_mean, label=f'{window}-Day Rolling Mean', color='red')
        plt.title('Publication Frequency with Rolling Mean')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_articles_by_hour(self):
        """Plot number of articles published by hour of day."""
        self.df['time_of_day'] = self.df['date'].dt.hour
        self.articles_by_hour = self.df['time_of_day'].value_counts().sort_index()
        plt.figure(figsize=(12, 6))
        sns.barplot(x=self.articles_by_hour.index, y=self.articles_by_hour.values, color='green')
        plt.title('Number of Articles by Hour of the Day')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Number of Articles')
        plt.tight_layout()
        plt.show()
