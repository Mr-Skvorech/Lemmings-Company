from strategy import Strategy
from finance_structures import *
from three_soldiers_strategy import *
from MinMaxStrategy import *
inf = 2e10

class LongShortTermStrategy(Strategy):
    def __init__(self, period, matter_period, feed_base, coef_not_factor=1.5):
        self.__init__("LongShortTermStrategy")
        self.short = MinMaxStrategy(period, matter_period, feed_base)
        self.long = ThreeSoldiersStrategy(period, matter_period, feed_base, coef_not_factor)

    def AddMoney(self, x):
        self.short.AddMoney(x / 3)
        self.long.AddMoney(x / 3 * 2)

    def Process(self, glass, curprice):
        return self.short.Process(glass, curprice) + self.long.Process(glass, curprice)
