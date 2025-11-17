class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)

    @property
    def quarter(self):
        month = int(self.date.split('-')[1])
        if 1 <= month <= 3:
            return "Q1"
        elif 4 <= month <= 6:
            return "Q2"
        elif 7 <= month <= 9:
            return "Q3"
        else:
            return "Q4"


def agg_crm_data(sells: str) -> str:
    sells_data = dict()
    for sell in sells.split(';'):
        item = Item(*sell.split(':'))
        data = sells_data.get(item.quarter, {})
        quantity = data.get(item.product, 0)
        data[item.product] = quantity + item.quantity
        sells_data[item.quarter] = data

    res = ''
    for k, v in sells_data.items():
        if res:
            res += ' '
        res += f'{k}: ' + ' - '.join([f'{product_name}: {quantity} '
                                     for product_name, quantity in v.items()])

    return res


for v in [
    '2023-01-15:Книга:10;2023-04-20:Флешка:5;2023-07-05:Наушники:8',
    '2023-02-05:Шляпа:4;2023-03-20:Кольцо:7;2023-04-25:Браслет:6;2023-04-26:Браслет:12',
]:

    print(v, '--> ', agg_crm_data(v), '\r\n')
