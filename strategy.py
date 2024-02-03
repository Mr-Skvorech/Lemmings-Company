from finance_structures import Candle, Order, Glass


#универсальный класс стратегии
class Strategy(object):
    #список всех свечек, зафиженый в стратегию
    feed = []
    total_money = 0

    #наименование стратегии
    strategy_name = "undefined"
    period = -1
    number_of_stocks = 0
    money = 0
    local_glass = Glass()
    refactor_time = 1
    cur_refactor_time = 0
    my_orders = []
    def __init__(self, nm, local_glass):
        self.feed = []
        self.strategy_name = nm
        self.local_glass = local_glass

    def __init__(self):
        self.feed = []
        self.strategy_name = "undefined"

    def OnRefactor(self):
        pass

    def Feed(self, cand):
        if (self.strategy_name == "undefined"):
            raise(BaseException("Undefined Behaviour: the strategy is either unnamed either undefined"))
        if (type(cand) != Candle):
            raise(BaseException("Type Error: attempt to feed non-candle to a Strategy template"))
        if (cand.is_undefined()):
            raise(BaseException("Undefined Behaviour: attempt to feed an undefined candle"))
        self.feed.append(cand)
        self.OnCandleAdded(cand)

    #не перегружать
    def Upd(self):
        if (self.strategy_name == "undefined"):
            raise("Undefined Behaviour: the strategy is undefined")
        if (self.total_money < self.money):
            total_money = money
        self.cur_refactor_time += 1
        if (self.cur_refactor_time > self.refactor_time):
            self.cur_refactor_time = 0
            self.RefactorMoney()
            self.OnRefactor()

    # должно вернуть список Order
    def Process(self, glass, curprice):
        if (self.strategy_name == "undefined"):
            raise("Undefined Behaviour: the strategy is undefined")
        pass

    def OnCandleAdded(self, candle):
        pass

    def AddMoney(self, x):
        self.money += x
        if (x > 0):
            self.total_money += x

    def AddStock(self, x):
        self.number_of_stocks += x

    def RefactorMoney(self):
        self.total_money = self.money

    def ValidateOrder(self, ord):
        if (ord.order_type == 0):
            self.AddMoney(ord.quantity * ord.price)
            self.AddStock(-ord.quantity)
        else:
            if (self.total_money * 0.0 < self.money):
                self.AddMoney(-ord.quantity * ord.price)
                self.AddStock(ord.quantity)

    def GetActiveMoney(self):
        return self.money

    def GetActiveStock(self):
        return self.number_of_stocks

    def GetNetForce(self, curprice):
        return self.money + self.number_of_stocks * curprice