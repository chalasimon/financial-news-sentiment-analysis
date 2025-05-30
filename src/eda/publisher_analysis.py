# src/eda/publisher_analysis.py

import re
import pandas as pd
import matplotlib.pyplot as plt

class PublisherAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.domain_counts = None
        self.publisher_earnings = None

    def extract_domains(self):
        """Extracts domains from email addresses in the 'publisher' column."""
        self.df['domain'] = self.df['publisher'].apply(lambda email: re.search(r'@([\w.-]+)', email).group(1) if pd.notnull(email) and re.search(r'@([\w.-]+)', email) else email)
        self.domain_counts = self.df['domain'].value_counts()
        return self.domain_counts

    def plot_top_domains(self, top_n=10):
        """Plots the top N contributing domains."""
        if self.domain_counts is None:
            self.extract_domains()
        plt.figure(figsize=(10, 6))
        self.domain_counts.head(top_n).plot(kind='bar')
        plt.title('Top Contributing Domains')
        plt.xlabel('Domain')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def identify_earnings_mentions(self):
        """Identifies headlines mentioning 'earnings' or 'profit'."""
        self.df['mention_earnings'] = self.df['headline'].apply(lambda x: bool(re.search(r'\b(earnings|profit)\b', str(x), re.IGNORECASE)))
        return self.df['mention_earnings'].sum()

    def earnings_by_publisher(self):
        """Analyzes earnings/profit mentions by publisher."""
        self.publisher_earnings = self.df[self.df['mention_earnings']].groupby('publisher').size()
        return self.publisher_earnings

    def plot_earnings_by_publisher(self, top_n=10):
        """Plots top publishers mentioning 'earnings' or 'profit'."""
        if self.publisher_earnings is None:
            self.earnings_by_publisher()
        plt.figure(figsize=(10, 6))
        self.publisher_earnings.head(top_n).plot(kind='bar')
        plt.title('Number of Articles Mentioning "Earnings" or "Profit" by Publisher')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
