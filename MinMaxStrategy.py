from strategy import Strategy
from finance_structures import *
inf = 2e10

class MinMaxStrategy(Strategy):
    refactor_time = 1
    localmin = inf
    localmax = -inf
    epsilon = 0.01
    #коффицент, с которым не учитываются 3 солдата
    def __init__(self, period, matter_period, feed_base):
        self.strategy_name = "MinMaxStrategy"
        self.period = period
        self.matter_peiod = matter_period
        for candle in feed_base:
            self.Feed(candle)
        self.Refactor_Bounds()

    def Refactor_Bounds(self):
        self.localmin = inf
        self.localmax = -inf
        for i in range(self.matter_peiod):
            self.localmin = min(self.localmin, self.feed[-i-1].low)
            self.localmax = max(self.localmax, self.feed[-i-1].high)

    def OnRefactor(self):
        Refactor_Bounds()

    def local_Process(self, glass, curprice):
        order = Order(0, 0, 0, 0)
        if (curprice < self.localmin + (self.localmax - self.localmin) * (1/3)):
            buy = min((self.money / 8), 0.10 * self.total_money) / curprice
            order = Order(buy, curprice, 1, -1)
        else:
            sell = (self.number_of_stocks / 2) / curprice
            order = Order(sell, curprice, 0, -1)
        self.ValidateOrder(order)
        return [order]


    def Process(self, glass, curprice):
        return self.local_Process(glass, curprice)