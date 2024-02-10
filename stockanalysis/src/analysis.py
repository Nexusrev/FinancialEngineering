import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StockAnalyzer:
    def __init__(self, data):
        '''
        Initializes the StockAnalyzer with stock data.
        
        Parameters:
        -  data: A pandas DataFrame with stock price data. Expected to have at least 'Close' column.
        '''
        self.data = data
    
    def calculate_sma(self, window=20):
        self.data[f'SMA_{window}'] = self.data['Close'].rolling(window=window).mean()
        return self.data[f'SMA_{window}']
    
    def calculate_ema(self, window=20):
        self.data[f'EMA_{window}'] = self.data['Close'].ewm(span=window,adjust=False).mean()
        return self.data[f'EMA_{window}']
    
    def calculate_momentum(self, window=10):
        self.data[f'Momentum_{window}'] = self.data['Close'].diff(periods=window)
        return self.data[f'Momentum_{window}']
    
    def calculate_volatility(self, window=20):
        self.data[f'Volatility_{window}'] = self.data['Close'].pct_change().rolling(window=window).std() * np.sqrt(window)
        return self.data[f'Volatility_{window}']
    
    def calculate_rsi(self, window=14):
        delta = self.data['Close'].diff(1)
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        self.data[f'RSI_{window}'] = 100 - (100 / (1 + rs))
        return self.data[f'RSI_{window}']
    
    def plot_indicators(self, indicators):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        for indicator in indicator:
            if indicator in self.data.columns:
                plt.plot(self.data[indicator], label=indicator)
        plt.title('Stock Price Indicators')
        plt.legend()
        plt.show()