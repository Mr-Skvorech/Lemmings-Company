from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods
from datetime import date
import shutil
import os
from PIL import Image
import mplfinance as mpf


def create_data(name_company, year_begin, month_begin, day_begin, year_end, month_end, day_end, inter):
    m1 = MoexImporter()
    sec = MoexSecurity(name_company, m1)
    is_exist = open('all companies.txt', 'r+')
    df_candles = sec.getCandleQuotesAsDataFrame(date(year_begin, month_begin, day_begin),
                                                date(year_end, month_end, day_end),
                                                interval=MoexCandlePeriods.Period1Day, board=None)
    df_candles = df_candles.drop('end', axis=1)
    df_string_close = df_candles["close"]
    df_string_close = df_string_close.to_string(header=False)
    df_string = df_candles.to_string(header=False)

    s = os.path.join('companies', name_company + ".txt")
    if name_company in is_exist.read():
        f = open(s, 'r+')
        f.truncate(0)
        f.close()
        my_file = open(s, "w")
        my_file.write(df_string)
        my_file.close()
    else:
        mf = open("all companies.txt", "a")
        mf.write(name_company + " ")
        mf.close()
        my_file = open(s, "w+")
        my_file.write(df_string)
        my_file.close()
    is_exist.close()
def load_graph_to_png(name_company, file_name, year_begin, month_begin, day_begin, year_end, month_end, day_end, inter):
    m1 = MoexImporter()
    file_name = "graphic.png"
    sec = MoexSecurity(name_company, m1)
    candles_df = sec.getCandleQuotesAsDataFrame(date(2023, 1, 1), date(2024, 1, 24),
                                                interval=MoexCandlePeriods.Period1Day, board=None)
    mpf.plot(candles_df, type="candle", mav=10, ylabel="price($)", figsize=(9.6,5.4),style="yahoo",
             savefig=file_name)
    im = Image.open(file_name)
    im.crop((170, 70, 900, 540)).save(file_name, quality=95)

    if os.path.exists(os.getcwd() + '/static/img' + '/' + file_name):
        os.remove(os.getcwd() + '/static/img' + '/' + file_name)
    shutil.move(file_name, os.getcwd() + '/static/img')


def generate_both(name_company):
    load_graph_to_png(name_company, name_company + ".png", 2023, 1, 1, 2024, 1, 1, 3)
    create_data(name_company, 2023, 1, 1, 2024, 1, 1, 3)
