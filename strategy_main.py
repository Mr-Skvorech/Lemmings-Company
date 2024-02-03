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
        date = datetime.today()
        date = date.split('-')

        self.data = create_candles(company, int(date[2]), int(date[1]), int(date[0]), int(date[2]) - 1, int(date[1]), int(date[0]), period)

    def Process(self):
        matter_peiod = 30
        feed_base = []
        for i in range(matter_peiod):
            feed_base.append(data[i])
        self.strategies = [MinMaxStrategy(self, self.period, matter_peiod, feed_base), ThreeSoldiersStrategy(self, matter_peiod, feed_base), LongShortTermStrategy(self)]
        graphs = []
        sovets = []
        curbest = -1
        curbestnetforce = -129830912380129
        id = 0
        for strategy in self.strategies:
            strategy.AddMoney(1e5)
            graphs.append([1e5 for i in range(matter_peiod)])
            for i in range(matter_peiod, len(data) - 1):
                strategy.Feed(data[i])
                strategy.Process(Glass(), data[i].close)
                graphs[-1].append(strategy.GetNetForce(data[i].close))
            strategy.Feed(data[-1])
            sovets.append(strategy.Process(Glass(), data[-1].close))
            if (curbestnetforce < strategy.GetNetForce(data[-1].close)):
                curbestnetforce = strategy.GetNetForce(data[-1].close)
                curbest = id
            id += 1
        return (graphs[id], sovets[id])

graph, sovet = abobus.Process()