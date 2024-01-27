from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods
from datetime import date
import shutil
import os
import mplfinance as mpf

def create_data(name_company, year_begin, month_begin, day_begin,year_end, month_end, day_end, inter):
    m1 = MoexImporter()
    sec = MoexSecurity(name_company, m1)
    is_exist = open('all companies.txt', 'r+')
    df_candles = sec.getCandleQuotesAsDataFrame(date(year_begin, month_begin, day_begin), date(year_end, month_end, day_end), interval=MoexCandlePeriods.Period1Day,  board=None)
    df_candles = df_candles.drop('end', axis=1)
    df_string = df_candles.to_string(header=False)
    s = name_company + ".txt"
    if name_company in is_exist.read():
        f = open(s, 'r+')
        f.truncate(0)
        f.close()
        my_file = open(s, "w")
        my_file.write(df_string)
        my_file.close()
    else:
        mf = open("all companies.txt", "a")
        mf.write(name_company+" ")
        mf.close()
        my_file = open(s, "w+")
        my_file.write(df_string)
        my_file.close()
    is_exist.close()

def load_graph_to_png(name_company, file_name, year_begin, month_begin, day_begin,year_end, month_end, day_end, inter):
    m1 = MoexImporter()
    sec = MoexSecurity(name_company, m1)
    candles_df = sec.getCandleQuotesAsDataFrame(date(2023, 1, 1), date(2024, 1, 24), interval=MoexCandlePeriods.Period1Day, board=None)
    mpf.plot(candles_df, type="candle", mav=10, style="yahoo", savefig=file_name)
    shutil.move(file_name, os.getcwd()+'/static/img')


def generate_both(name_company):
    if not(os.path.exists(os.getcwd() + '/static/img/' + name_company + '.png')):
        load_graph_to_png(name_company, name_company+".png", 2023,1,1,2024,1,1,3)
    if not(os.path.exists(os.getcwd() + name_company + '.txt')):
        create_data(name_company, 2023,1,1,2024,1,1,3)

if __name__ == "__main__":
    generate_both("SBER")
