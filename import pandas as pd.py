import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

yahoo_financials = YahooFinancials('TSLA')
data = yahoo_financials.get_historical_price_data(start_date='2019-01-01',
end_date= '2019-12-21',
time_interval='weekly')

print(data)