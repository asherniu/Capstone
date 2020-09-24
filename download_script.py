import Config

import pandas_datareader.data as web

from datetime import datetime


def download(code):
    """
    Download the stock data from Investor's Exchange API and save it as csv
    :param code: stock code
    :return: null
    """
    try:
        print(f"Downloading stock {code}")
        df = web.DataReader(code, 'iex', start_date, end_date, api_key=Config.IEX_API)
        output = code + ".csv"
        df.to_csv(output)
    except Exception as err:
        print(f"Downloading stock {code} failed")
        print(err)


def download_yahoo(code):
    """
    Download the stock data from Yahoo API and save it as csv
    It is better since it has higher limits
    :param code: stock code
    :return: null
    """
    try:
        print(f"Downloading stock {code}")
        df = web.DataReader(code, 'yahoo', start_date, end_date)
        output = code + ".csv"
        df.to_csv(output)
    except Exception as err:
        print(f"Downloading stock {code} failed")
        print(err)


if __name__ == '__main__':
    """Set the start and end time of historical data"""
    start_date = datetime(2015, 11, 1)
    end_date = datetime(2019, 11, 1)
    print(f"The start date is set to {start_date}, and the end date is set to {end_date}")

    """Free account can only download about 3 stocks per month."""
    codes = ['MSFT', 'AMZN','AAPL', 'FB', 'GOOGL']
    print(f"The stocks code I will be downloading are {codes}")

    for code in codes:
        download_yahoo(code)
