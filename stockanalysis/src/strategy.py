import numpy as np 

class MovingAverageCrossoverStrategy:
    def __init__(self, short_window=40, long_window=100):
        self.short_window = short_window
        self.long_window = long_window

    def signal(self, data):
        """Generates trading signals."""
        signals = np.zeros(data.shape[0])
        short_ma = data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        long_ma = data['Close'].rolling(window=self.long_window, min_period=1).mean()
        signals[short_ma > long_ma] = 1
        signals[short_ma < long_ma] = -1 
        return signals
    