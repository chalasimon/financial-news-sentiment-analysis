import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Corr_Visualization:
    def __init__(self, data):
        self.data = data
    def stock_price(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['Close'], label='Close Price', color='blue')
        plt.title(f'Stock Price Over Time for {self.data["Stock"].iloc[0]}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
