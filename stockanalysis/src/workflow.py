import yfinance as yf
from analysis import StockAnalyzer
from backtesting import Backtester
from strategies import MovingAverageCrossoverStrategy
# from ml_model import StockPriceDirectionPredictor  # Assuming you've added features for ML predictions

# Fetch and prepare data
data = yf.download('AAPL', start='2019-01-01', end='2020-12-31')

# Analysis (optional step for feature engineering)
analyzer = StockAnalyzer(data)
analyzer.calculate_sma(20)
analyzer.calculate_ema(50)

# Strategy
strategy = MovingAverageCrossoverStrategy(short_window=20, long_window=50)

# Backtesting
backtester = Backtester(data, strategy)
backtester.run()
backtester.plot_results()

# ML Prediction (optional)
# predictor = StockPriceDirectionPredictor(data)
# predictor.train_model()
