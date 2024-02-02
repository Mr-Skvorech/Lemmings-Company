
PeriodNames = dict()
PeriodNames[0] = "1 минута"
PeriodNames[1] = "10 минут"
PeriodNames[2] = "1 час"
PeriodNames[3] = "1 день"
PeriodNames[4] = "1 неделя"
PeriodNames[5] = "1 месяц"
PeriodNames[6] = "3 месяца"


class Candle(object):
    # 0 - 1 минута
    # 1 - 10 минут
    # 2 - 1 час
    # 3 - 1 день
    # 4 - 1 неделя
    # 5 - 1 месяц
    # 6 - 3 месяца
    # -1 - undefined
    period = 1
    open = -1
    close = -1
    high = -1
    low = -1

    def __init__(self, open, close, high, low):
        self.open = open
        self.close = close
        self.high = high
        self.low = low

    def is_undefined(self):
        return self.open == -1 or self.close == -1 or self.high == -1 or self.low == -1


class Order(object):
    quantity = 0
    price = 0
    id = 0
    # 0 - продажа
    # 1 - покупка
    order_type = 0

    def __init__(self, quantity, price, order_type, id):
        self.price = price
        self.quantity = quantity
        self.order_type = order_type
        self.id = id

    def is_undefined(self):
        return self.quantity == 0


class Glass(object):
    sells = dict()
    buys = dict()
    new_buy_id = 0
    new_sell_id = 0

    def __init__(self):
        pass

    def AddOrder(self, order):
        if (order.order_type == 0):
            self.sells[self.new_sell_id] = order
            self.new_sell_id += 1
            return self.new_sell_id - 1
        else:
            self.buys[self.new_buy_id] = order
            self.new_buy_id += 1
            return self.new_buy_id - 1
        return -1

    def DelOrder(self, order_id, order_type):
        if (order_type == 0):
            self.sells[order_id] = Order(0, 0, 0)
        else:
            self.buys[order_id] = Order(0, 0, 1)



