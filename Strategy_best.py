import matplotlib.pyplot as plt
from shutil import move
import matplotlib
matplotlib.use('AGG')
from datetime import date
import os
from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods
from matplotlib.dates import DateFormatter
from strategy_main import *
from finance_structures import Candle
def Strategy_visualization(name_company, year_begin, month_begin, day_begin, year_end, month_end, day_end, inter):
    ax = plt.axes()
    file_name = "strategia.png"
    print(file_name)
    company = CompanyManager(name_company, 3)
    networth, soveti, lenth = company.Process()
    date_begin = date(2022, 1, 1)
    dates = list()
    for i in range(lenth-1):
        dates.append(date_begin)
        date_begin += timedelta(days=1)

    ax.plot(dates, networth)
    fmt = matplotlib.dates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(fmt)
    if os.path.exists(os.getcwd() + '/static/img' + '/' + file_name):
        os.remove(os.getcwd() + '/static/img' + '/' + file_name)
    plt.savefig(file_name)
    move(file_name, os.getcwd() + '/static/img')
    plt.close()
    return (networth, soveti, lenth)