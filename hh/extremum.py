import re
import sys
from typing import Literal

ExtremumType = Literal['min', 'max']


class Window:
    def __init__(self, size, data):
        self.left = 0
        self.size = size
        self.i_min = self.i_max = 0
        self.mid = int(size / 2)
        self.data = data
        self.res = []

    def calc_window(self):
        min = sys.float_info.max
        max = sys.float_info.min
        self.mid = int(self.left + self.size / 2)

        for i in range(self.left + self.size):
            self.curr = self.data[i]
            if self.curr < min:
                min = self.curr
                self.i_min = i
            if self.curr > max:
                max = self.curr
                self.i_max = i

        self.left += 1

    def eval_extremum(self):
        if self.i_min == self.mid:
            self.res.append(('min', self.data[self.mid]))
        if self.i_max == self.mid:
            self.res.append(('max', self.data[self.mid]))

    def process(self):
        i = len(self.data) - self.size
        while i > 0:
            i -= 1
            self.calc_window()
            self.eval_extremum()


def find_local_extremums(
    widow_half_size: int,
        data: list[float]) -> list[tuple[ExtremumType, float]]:
    full_size = 2 * widow_half_size + 1

    if len(data) < full_size:
        return []

    w = Window(full_size, data)
    w.process()

    return w.res


input_ex = re.compile(r'^\s*(\d+)\s+(.+)\s*$')


def parce_input(data):
    m = input_ex.match(data)
    if m is None:
        raise ValueError(f'Illegal data: {data}')
    if len(m.groups()) < 2:
        raise ValueError(f'Illegal data: {data}')

    return int(m.group(1)), [float(v) for v in m.group(2).split(',')]


for v in [
    '2 0.891,0.987,0.995,0.969,0.7,0.128',
    '1 0.73727,2.96021,3.45525,4.6196,7.17337,9.91429,5.22745,4.58553,0.930094,8.21642',
        '1 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9']:

    res = find_local_extremums(*parce_input(v))
    print(res if len(res) else 'Экстремумов не обнаружено')
    # print(parce_input(v))
