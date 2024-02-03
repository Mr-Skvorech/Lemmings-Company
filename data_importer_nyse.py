import matplotlib.pyplot as plt 
from mpl_finance import candlestick_ohlc 
import mplfinance as mpf
import pandas as pd 
import matplotlib.dates as mpl_dates 
import numpy as np 
import datetime
import yfinance as yf
from yahoofinancials import YahooFinancials
from PIL import Image
import os
import shutil
import csv

def from_csv_to_txt(csv_file, txt_file):
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

def relocate_data(txt1_file, txt2_file):
    with open(txt1_file, "r") as input: 
        with open(txt2_file, "w") as output:
            for line in input: 
                output.write(line)

def load_graph_to_png(name_company, file_name, year_begin, month_begin, day_begin, year_end, month_end, day_end, inter):
    # m1 = MoexImporter()
    # file_name = "graphic.png"
    # sec = MoexSecurity(name_company, m1)
    # candles_df = sec.getCandleQuotesAsDataFrame(date(2023, 1, 1), date(2024, 1, 24),
    #                                             interval=MoexCandlePeriods.Period1Day, board=None)
    file_name = "graphic.png"
    df_candles = yf.download(name_company, start=datetime.datetime(year_begin, month_begin, day_begin), 
                             end=datetime.datetime(year_end, month_end, day_end), progress=False)
    mpf.plot(df_candles, type="candle", mav=10, ylabel="price($)", figsize=(19.2,10.8),style="yahoo",
             savefig=file_name)
    im = Image.open(file_name)
    im.crop((340, 140, 1800, 1000)).save(file_name, quality=95)
    path_f = os.getcwd() + '/static/img/' + file_name
    if os.path.exists(path_f):
        os.remove(path_f)
    shutil.move(file_name, os.getcwd() + '/static/img/')

def create_data(name_company, year_begin, month_begin, day_begin, year_end, month_end, day_end, inter):
    is_exist = open('all companies.txt', 'r+')
    df_candles = yf.download(name_company, start=datetime.datetime(year_begin, month_begin, day_begin), 
                             end=datetime.datetime(year_end, month_end, day_end), progress=False)
    df_candles.to_csv("data_nyse.csv")
    from_csv_to_txt("data_nyse.csv", "data_nyse.txt")

    s = os.path.join('companies', name_company + ".txt")
    if name_company in is_exist.read():
        relocate_data("data_nyse.txt", s)
    else:
        mf = open("all companies.txt", "a")
        mf.write(name_company + " ")
        mf.close()
        relocate_data("data_nyse.txt", s)
    is_exist.close()

def generate_both_NYSE(name_company):
    load_graph_to_png(name_company, name_company + ".png", 2023, 1, 1, 2024, 1, 1, 3)
    create_data(name_company, 2023, 1, 1, 2024, 1, 1, 3)

if __name__ == "__main__":
    generate_both_NYSE("AAPL")