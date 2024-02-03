from contourpy.util import data
from strategy import *
from finance_structures import *

from MinMaxStrategy import *
from three_soldiers_strategy import *
from LongShortTerm import *

from datetime import *

from open_close_high_low_import import *

class CompanyManager(object):
    strategies = []
    data = []
    company = "undefined"
    period = 3
    def __init__(self, company, period):
        self.company = company
        self.period = period
        date_s = datetime.today().strftime('%Y-%m-%d')
        date_s = date_s.split('-')

        self.data = create_candles(self.company, int(date_s[0])-2, int(date_s[1]), int(date_s[2]), int(date_s[0]), int(date_s[1]), int(date_s[2]), period)

    def Process(self):
        matter_peiod = 30
        feed_base = []
        print(len(self.data))
        for i in range(matter_peiod):
            feed_base.append(self.data[i])
        self.strategies =  [MinMaxStrategy(self.period, matter_peiod, feed_base), ThreeSoldiersStrategy(self.period,matter_peiod, feed_base), LongShortTermStrategy(self.period,matter_peiod, feed_base)]
        graphs = []
        sovets = []
        curbest = -1
        curbestnetforce = -129830912380129
        id = 0
        for strategy in self.strategies:
            strategy.AddMoney(1e5)
            graphs.append([1e5 for i in range(matter_peiod)])
            for i in range(matter_peiod, len(self.data) - 1):
                strategy.Feed(self.data[i])
                strategy.Process(Glass(), self.data[i].close)
                graphs[-1].append(strategy.GetNetForce(self.data[i].close))
            strategy.Feed(self.data[-1])
            sovets.append(strategy.Process(Glass(), self.data[-1].close))
            if (curbestnetforce < strategy.GetNetForce(self.data[-1].close)):
                curbestnetforce = strategy.GetNetForce(self.data[-1].close)
                curbest = id
            id += 1
        return (graphs[id-1], sovets[id-1], len(self.data))