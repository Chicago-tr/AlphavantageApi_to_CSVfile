# AlphavantageApi_to_CSVfile

Simple script for making an Alphavantage Api request and saving the results to a csv file using python. The script will request adjusted daily time series data (OHLCV) for the past 20 years on equities given a list of ticker symbols and an API key. It saves each call as a csv file in the directory the script is run from. Modifying the 'function' variable allows for making different API requests.
