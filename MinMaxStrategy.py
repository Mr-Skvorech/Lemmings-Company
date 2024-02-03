from strategy import Strategy
from finance_structures import *
from math import sqrt
inf = 2e10

class MinMaxStrategy(Strategy):
    refactor_time = 30
    localmin = inf
    localmax = -inf
    epsilon = 0.01
    #коффицент, с которым не учитываются 3 солдата
    def __init__(self, period, matter_period, feed_base):
        self.strategy_name = "MinMaxStrategy"
        self.period = period
        self.matter_period = matter_period
        for candle in feed_base:
            self.Feed(candle)
        self.Refactor_Bounds()

    def Refactor_Bounds(self):
        self.localmin = inf
        self.localmax = -inf
        for i in range(self.matter_period):
            self.localmin = min(self.localmin, self.feed[-i-1].low)
            self.localmax = max(self.localmax, self.feed[-i-1].high)

    def OnRefactor(self):
        Refactor_Bounds()

    def local_Process(self, glass, curprice):
        self.Refactor_Bounds()
        avg = 0
        dev = 0
        for  i in range(1, self.matter_period + 1):
            avg += self.feed[-i].close
            dev += abs((self.feed[-i].close - self.feed[-i].open) / self.feed[-i].close)
        avg /= self.matter_period
        dev /= self.matter_period

        order = Order(0, 0, 0, 0)
        target_price = self.localmin + (self.localmax - self.localmin) * (min(self.GetActiveMoney() / (2 * self.GetNetForce(curprice)), 1/16))
        gr = (self.feed[-1].close - self.feed[-10].open) / curprice

        print("AVG:", avg)
        print("CURRENT", curprice)

        if (avg * 1.1 > curprice):
            money_buy = min((self.money / 16), 5e3)
            avg_mult = sqrt(0.8 * avg / curprice)
            print(dev)
            dev_mult = (dev ** (1 / 3))
            print("AVG MULTIPLICATOR:", avg_mult)
            print("DEV MULTIPLICATOR:", dev_mult)
            buy = money_buy * avg_mult / curprice
            buy *= self.GetActiveMoney() / self.GetNetForce(avg)
            print("BUY", buy)
            order = Order(buy, curprice, 1, -1)
        else:
            self.localmin = curprice
            sell = (2 * self.number_of_stocks / 3) / curprice
            order = Order(sell, curprice, 0, -1)
        self.ValidateOrder(order)
        return [order]


    def Process(self, glass, curprice):
        return self.local_Process(glass, curprice)
