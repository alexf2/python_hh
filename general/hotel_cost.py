import datetime
import locale
from decimal import Decimal

locale.setlocale(locale.LC_ALL, 'ru_RU')

weekday_cost = Decimal(1500)
weekend_cost = Decimal(1900)


def calc_cost(date_from, date_to) -> float:
    date_curr = date_from
    cost = Decimal(0)
    w = we = 0
    delta = datetime.timedelta(days=1)

    while date_curr <= date_to:
        if date_curr.weekday() in (5, 6):
            we += 1
            cost += weekend_cost
        else:
            w += 1
            cost += weekday_cost

        date_curr = date_curr + delta

    return cost, w, we


for dt1, dt2 in (
    (datetime.date(
        2025, 5, 2), datetime.date(
            2025, 5, 7)), (datetime.date(
                2025, 6, 11), datetime.date(
                    2025, 6, 17))):

    cost, w, we = calc_cost(dt1, dt2)

    print(dt1.strftime("%Y-%B-%d"), '-->', dt2.strftime("%Y-%B-%d"), ' = ',
          f'{cost:,.2f}'.rstrip('0').rstrip('.') + ' ₽', 'w=', w, 'we=', we)
