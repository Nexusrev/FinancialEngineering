import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    '''
    
    Feteches historical stock prices for a givern ticket & time range/frame.
    
    Parameters:
    - ticker: The stock symbol to fetch data for ( ex: 'SPY').
    - start_date: The start date for the data (format: 'YYYY-MM-DD').
    - end_date: The end date for the data (format: 'YYYY-MM-DD').
    
    Returns:
    A pandas DF w/ the historical stock prices.
    '''

    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

if __name__ == "__main__":
    
    # Example
    ticker = 'SPY'
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    data = fetch_stock_data(ticker, start_date, end_date)
    print(data.head())