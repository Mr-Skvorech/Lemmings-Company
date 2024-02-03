import matplotlib.pyplot as plt
import shutil
import datetime
from datetime import date
import os
from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods
import matplotlib.dates as mdates
from strategy_main import *
from finance_structures import Candle
periods = dict()
periods[3] = MoexCandlePeriods.Period1Day
periods[4] = MoexCandlePeriods.Period1Week
periods[5] = MoexCandlePeriods.Period1Month
periods[6] = MoexCandlePeriods.Period1Quarter
def create_candles(name_company, year_begin, month_begin, day_begin, year_end, month_end, day_end, period):
    m1 = MoexImporter()
    sec = MoexSecurity(name_company, m1)
    df_candles = sec.getCandleQuotesAsDataFrame(date(year_begin, month_begin, day_begin), date(year_end, month_end, day_end), interval=periods[period],  board=None)
    df_candles = df_candles.drop(labels='end', axis=1)
    df_candles = df_candles.drop(labels='quantity', axis=1)
    df_candles = df_candles.drop(labels='value', axis=1)
    df_string = df_candles.to_string(header=False)
    ds_spl = df_string.split()
    e = 0
    khanda = []
    for i in range(2, len(ds_spl), 5):
        khanda.append(Candle(float(ds_spl[i]), float(ds_spl[i+1]),float(ds_spl[i+2]),float(ds_spl[i+3])))
    return khanda
def Strategy_visualization(name_company, year_begin, month_begin, day_begin, year_end, month_end, day_end, inter):
    ax = plt.axes()
    file_name = "strategy.png"
    company = CompanyManager(name_company, 3)
    networth, soveti, lenth = company.Process()
    date_begin = date(2022, 1, 1)
    dates = list()
    for i in range(lenth-1):
        dates.append(date_begin)
        date_begin += timedelta(days=1)

    ax.plot(dates, networth)
    fmt = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(fmt)
    plt.savefig(file_name)
    if os.path.exists(os.getcwd() + '/static/img' + '/' + file_name):
        os.remove(os.getcwd() + '/static/img' + '/' + file_name)
    #shutil.move(file_name, os.getcwd() + '/static/img')


Strategy_visualization("SBER", 2022,1,1,2024,1,1,3)

