import os
import pandas as pd
from pathlib import Path
from typing import Optional, Dict, Any
import numpy as np
import talib 

class QuantitativeAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        
    def calculate_SMA(self, column: str, window: int) -> pd.Series:
        # Calculate Simple Moving Average (SMA) for a given column.
        return talib.SMA(self.df[column], timeperiod=window)
    def calculate_EMA(self, column: str, window: int) -> pd.Series:
        # Calculate Exponential Moving Average (EMA) for a given column.
        return talib.EMA(self.df[column], timeperiod=window)
    def calculate_RSI(self, column: str, window: int) -> pd.Series:
        # Calculate Relative Strength Index (RSI) for a given column.
        return talib.RSI(self.df[column], timeperiod=window)
    def calculate_MACD(self, column: str) -> pd.DataFrame:
        # Calculate Moving Average Convergence Divergence (MACD) for a given column.
        macd, macdsignal, macdhist = talib.MACD(self.df[column], fastperiod=12, slowperiod=26, signalperiod=9)
        return pd.DataFrame({
            'macd': macd,
            'macdsignal': macdsignal,
            'macdhist': macdhist
        })
    def calculate_daily_returns(self, column: str) -> pd.Series:
        # Calculate daily returns for a given column.
        return self.df[column].pct_change().dropna()
    def calculate_volatility(self, column: str, window: int) -> pd.Series:
        # Calculate rolling volatility (standard deviation) for a given column.
        return self.df[column].rolling(window=window).std().dropna()
    