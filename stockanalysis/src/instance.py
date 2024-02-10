import yfinance as yf
from analysis import StockAnalyzer

# Fetching data
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-01-01'
data = yf.download(ticker, start=start_date, end=end_date)

# Initializing
analyzer = StockAnalyzer(data)

# Calculate indicators
analyzer.calculate_sma(20)
analyzer.calculate_ema(20)
analyzer.calculate_momentum(10)
analyzer.calculate_volatility(20)
analyzer.calculate_rsi(14)

# Option to plot indicators
analyzer.plot_indicators(['SMA_20', 'EMA_20', 'RSI_14'])