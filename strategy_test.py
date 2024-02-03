from strategy import *
from finance_structures import *
from three_soldiers_strategy import *
from MinMaxStrategy import *
from LongShortTerm import *
from open_close_high_low_import import *


#SBER BANE
def main():
    matter_period = 200
    period = 3
    capital = 1e5
    data = create_candles("SBER", 2022, 1, 1, 2024, 1, 1, period)
    feed_base = []
    for i in range(matter_period):
        feed_base.append(data[i])
    test = MinMaxStrategy(period, matter_period, feed_base)
    test.AddMoney(capital)
    for i in range(matter_period, len(data)):
        test.Feed(data[i])
        test.Process(Glass(), data[i].close)
        if (i % 1 == 0):
            print(str(test.GetActiveMoney()) + " + "  + str(test.GetActiveStock()) + " per " + str(data[i].close) + ": ", end = " ")
            print(test.GetActiveMoney() + test.GetActiveStock() * data[i].close)
    print(test.GetActiveMoney() + test.GetActiveStock() * data[-1].close)

if __name__ == '__main__':
    main()