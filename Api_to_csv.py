#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


def dailydata_csv(symbol_list, key):

    function = "TIME_SERIES_DAILY_ADJUSTED"
    output_size = "full" # Optional, "compact" by default, "full" for full history
    data_type = "csv" # for specifying csv output

    for symbol in symbols_list:
        
        url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}&outputsize={output_size}&datatype={data_type}"
        response = requests.get(url)

        if response.status_code == 200:
            # Successful response code
            csv_data = response.text
            
            with open(f"{symbol}_daily.csv", "w") as file:
                file.write(csv_data)
                print(f"CSV data saved to {symbol}_daily.csv")

        else:
            #Unsuccessful response code
            print(f"Error: {response.status_code}")
            print(response.text)


if __name__ == '__main__':

    symbols_list = ['List of ticker symbols to obtain data for']
    key= "Alphavantage Api Key"

    dailydata_csv(symbols_list, key)
