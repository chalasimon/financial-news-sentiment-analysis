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
        """Extracts and counts domains from email addresses in 'publisher'."""
        self.df['domain'] = self.df['publisher'].apply(
            lambda x: re.search(r'@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', str(x)).group(1).lower() 
            if pd.notnull(x) and re.search(r'@', str(x)) 
            else x
        )
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
       # Identifies headlines mentioning 'earnings' or 'profit'.
        self.df['mention_earnings'] = self.df['headline'].str.contains(r'\b(earnings|profit)\b', case=False, regex=True)
        return self.df['mention_earnings'].sum()

    def earnings_by_publisher(self, n=10):
        """Analyzes earnings/profit mentions by publisher."""
            # Get top publishers
        top_publishers = (
            self.df[self.df['mention_earnings']]  # Filter to earnings mentions
            .groupby('publisher')                 # Group by publisher
            .size()                               # Count occurrences
            .nlargest(n)                          # Get top N
            .rename('earnings_mentions')          # Rename for clarity
        )

        self.publisher_earnings = top_publishers

        return top_publishers

    def plot_earnings_by_publisher(self, top_n=10):
        """Plots top publishers mentioning 'earnings' or 'profit'."""
        if self.publisher_earnings is None:
            self.earnings_by_publisher(10)
        plt.figure(figsize=(10, 6))
        self.publisher_earnings.head(top_n).plot(kind='bar')
        plt.title('Number of Articles Mentioning "Earnings" or "Profit" by Publisher')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
