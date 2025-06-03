import seaborn as sns
import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, data):
        self.data = data

    # Plot Close Price and Moving Averages
    def plot_price_moving_averages(self,ticker: str):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['Close'], label='Close Price', color='blue')
        plt.plot(self.data['Date'], self.data['SMA20'], label='20-Day SMA', color='red')
        plt.plot(self.data['Date'], self.data['EMA'], label='20-Day EMA', color='green')
        plt.title(f'{ticker} Close Price and Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
    # Plot RSI
    def plot_rsi(self, ticker: str):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['RSI'], label='RSI', color='purple')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')
        plt.title(f'{ticker} RSI')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.legend()
        plt.show()
    # Plot MACD
    def plot_macd(self, ticker: str):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['MACD'], label='MACD', color='blue')
        plt.plot(self.data['Date'], self.data['MACD_signal'], label='MACD Signal', color='orange')
        plt.bar(self.data['Date'], self.data['MACD_hist'], label='MACD Histogram', color='gray', alpha=0.5)
        plt.title(f'{ticker} MACD')
        plt.xlabel('Date')
        plt.ylabel('MACD')
        plt.legend()
        plt.show()
    # Plot Volatility
    def plot_volatility(self, ticker: str):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['Volatility'], label='Volatility', color='brown')
        plt.title(f'{ticker} Volatility')
        plt.xlabel('Date')
        plt.ylabel('Volatility')
        plt.legend()
        plt.show()
    # Plot Daily Returns
    def plot_daily_returns(self, ticker: str):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['DailyReturns'], label='Daily Returns', color='cyan')
        plt.title(f'{ticker} Daily Returns')
        plt.xlabel('Date')
        plt.ylabel('Daily Returns')
        plt.legend()
        plt.show()
