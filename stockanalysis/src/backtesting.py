import pandas as pd 

class Backtester:
    def __init__(self, data, strategy, initial_capital=10000):
        '''
        Initializes the Backtester.

        Parameters:
        - data: a pandas Dataframe with stock price data.
        - strategy: An instance of a trading strategy class with a 'signal' method.
        - initial_capital: The initial capital in dollars.
        '''
        self.data = data
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.results = None

    def run(self):
        """Execute the backtesting of the strategy."""
        self.data['signal'] = self.strategy.signal(self.data)
        self.data['positions'] = self.data['signal'].diff()

        # Simulate trades and calculate equity curve
        self.data['portfolio'] = self.initial_capital * (1 + (self.data['signal'] * self.data['Close'].pct_change())).cumprod()
        self.results = self.data

    def plot_results(self):
        """Plots the performance of the strategy compared to the stock itself. """
        if self.results is None:
            print("No backtesting results to plot.")
            return
        
        self.results[['Close', 'portfolio']].plot(figsize=(10, 6))
        