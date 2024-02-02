from strategy import Strategy
from finance_structures import *
inf = 2e10

class ThreeSoldiersStrategy(Strategy):
    refactor_time = 10
    localmin = inf
    localmax = -inf
    epsilon = 0.01
    #коффицент, с которым не учитываются 3 солдата
    coef_not_factor = 1.5
    investements = []
    def __init__(self, period, matter_period, feed_base, coef_not_factor=1.5):
        self.__init__("ThreeSoldiersStrategy")
        self.period = period
        self.matter_peiod = matter_period
        for candle in feed_base:
            self.Feed(candle)
        self.Refactor_Bounds()

    def Refactor_Bounds(self):
        self.localmin = inf
        self.localmax = -inf
        for i in range(self.matter_peiod):
            mn = min(self.localmin, self.feed[-i-1].low)
            mx = max(self.localmax, self.feed[-i-1].high)

    def OnRefactor(self):
        Refactor_Bounds()

    def local_Process(self, glass, curprice):
        if (2 * curpice > self.localmin + self.localmax):
            self.localmax += 1 * (curpice - self.localmin)
        first = self.feed[-3]
        second = self.feed[-2]
        third = self.feed[-1]
        buy = (money / 4) / curprice
        sell = 0
        if (first.open - first.close > 0):
            buy = 0
        if (second.open - second.close > 0):
            buy = 0
        if (third.open - third.close > 0):
            buy = 0
        if ((third.open - third.close) / (second.open - second.close) > coef_not_factor):
            buy = 0
        orderbuy = Order(buy, curpirce, 1, -1)
        self.ValidateOrder(orderbuy)
        ans = []

        ans.append(orderbuy)
        investements.append(Order(buy, self.localmax, 0, -1))
        neewinv = []
        for inv in investments:
            if (abs(curpice - inv.price) / curprice < epsilon):
                ordersell = Order(curprice, inv.quantity, 0, -1)
            else:
                newinv.append(inv)
        inv = newinv


    def Process(self, glass, curprice):
        return local_Process(self, glass, curprice)
