from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods
from datetime import date
from finance_structures import *

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

